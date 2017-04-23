# script para geração da métrica LPC - Local Potencial Contribution and GPC - Global Potencial Contribution

# será gerado um arquivo contendo os valores da métrica por par de usuários
# adicionalmente, será gerado um segundo arquivo com todas as opções de cálculo disponíveis
# o arquivo gerado para a métrica SR é utilizado no cálculo da CT

# cabeçalho do arquivo gerado (CT.csv):
# 0 - programming_language_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - CT (CT_AN)

# cabeçalho do arquivo gerado (CT_all_options.csv):
# 0 - programming_language_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - CT_PR
# 4 - CT_AN

import sys, csv, operator, collections

# cria dict com os valores de SR para cada par de usuários da rede
SR_metric = {}

print("Reading SR.csv...")
with open('../Files/SR.csv', 'r') as r:
	SR_file = csv.reader(r, delimiter=',')

	next(SR_file) # cabeçalho
	# programming_language_id, developer_id_1, developer_id_2, SR

	for row in SR_file:
		prog_lang_id = int(row[0])
		dev1 = int(row[1])
		dev2 = int(row[2])
		SR = int(row[3])

		SR_metric[prog_lang_id, dev1, dev2] = SR
r.close()
print("Finished read SR.csv")

# cria dict com os repositórios da rede com sua linguagem e suas quantidades de linhas adicionadas e deletadas
rep_dict_language = {}

print("Reading repository.csv...")
with open('../DataSet/repository.csv', 'r') as r:
	repositories = csv.reader(r, delimiter=',')

	next(repositories) # cabeçalho
	# repository_id,name,description,programming_language_id,url,create_date,end_date,duration_days,number_add_lines,number_del_lines,number_commits,number_commiters

	for row in repositories:
		rep_id = int(row[0])
		prog_lang_id = int(row[3])
		duration_days = int(row[7])

		# inclui no dict cada repositório, o id da sua linguagem e o tempo de duração do mesmo
		rep_dict_language[rep_id] = [prog_lang_id, duration_days]
r.close()
print("Finished read repository.csv")

# lê informações da rede realizando os cálculos para a métrica
CT_metric = {}

print("Reading developers_social_network.csv...")
with open('../DataSet/developers_social_network.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,begin_contribution_date,end_contribution_date,contribution_days,number_add_lines,number_del_lines,number_commits

	for row in data:
		rep_id = int(row[0])

		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		contribution_days = int(row[5])
		
		prog_lang_id = rep_dict_language[rep_id][0]
		rep_duration_days = rep_dict_language[rep_id][1]

		# calcula as possibilidades da métrica
		CT_PR = 0 if rep_duration_days == 0 else contribution_days / rep_duration_days
		CT_AN = contribution_days
			
		# cria um dict com cada par de desenvolvedores e o valor dos cálculos para eles
		# key = (programming_language_id, dev1, dev2) values = CT_PR, CT_AN
		if (prog_lang_id, dev_1_id, dev_2_id) in CT_metric:
			total_CT_PR = CT_metric[prog_lang_id, dev_1_id, dev_2_id][0] + CT_PR
			total_CT_AN = CT_metric[prog_lang_id, dev_1_id, dev_2_id][1] + CT_AN
			
			CT_metric[prog_lang_id, dev_1_id, dev_2_id] = [total_CT_PR, total_CT_AN]
		else:
			CT_metric[prog_lang_id, dev_1_id, dev_2_id] = [CT_PR, CT_AN]
r.close()

# ordena dict da métrica
print("Sorting CT metric dict...")
CT = collections.OrderedDict(sorted(CT_metric.items()))

# cria dict com tempo máximo de contribuição por linguagem
max_time_per_language = {}
print("Selecting max contribution time per programming language...")
for row in CT:
	prog_lang_id = row[0]

	if prog_lang_id in max_time_per_language:
		if max_time_per_language[prog_lang_id] < CT[row][1]:
			max_time_per_language[prog_lang_id] = CT[row][1]
	else:
		max_time_per_language[prog_lang_id] = CT[row][1]

# escreve todos os dados da métrica no arquivo final com métrica única
print("Writing CT.csv...")
with open('../Files/CT.csv', 'w') as w:
	metric_file = csv.writer(w, delimiter=',')

	# escreve cabeçalho
	metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "CT"])

	# a soma do tempo de contribuição é dividida pelo tempo total da rede
	for row in CT:
		prog_lang_id = row[0]
		metric_file.writerow([prog_lang_id, row[1], row[2], CT[row][1]/max_time_per_language[prog_lang_id]])
w.close()

# escreve todos os dados da métrica no arquivo final com todas as opções
print("Writing CT_all_options.csv...")
with open('../Files/CT_all_options.csv', 'w') as w:
	metric_file = csv.writer(w, delimiter=',')

	# escreve cabeçalho
	metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "CT_PR", "CT_AN"])

	# CT_PR: a soma dos valores da métrica é dividida pelo número de repositórios compartilhados entre os desenvolvedores (SR)
	# CT_AN: a soma do tempo de contribuição é dividida pelo tempo total da rede
	for row in CT:
		prog_lang_id = row[0]
		metric_file.writerow([prog_lang_id, row[1], row[2], CT[row][0]/SR_metric[row], CT[row][1]/max_time_per_language[prog_lang_id]])
w.close()