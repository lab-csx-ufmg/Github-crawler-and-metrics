# script para geração da métrica JCSR - Jointly Developers Contribution to Shared Repositories

# será gerado um arquivo contendo os valores da métrica por par de usuários
# o arquivo gerado para a métrica SR é utilizado no cálculo da JCSR

# cabeçalho da arquivo gerado (JCSR.csv):
# 0 - programming_language_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - JCSR

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

# cria dict com os repositórios da rede com sua linguagem e sua quantidade de commiters
rep_dict_language = {}

print("Reading repository.csv...")
with open('../DataSet/repository.csv', 'r') as r:
	repositories = csv.reader(r, delimiter=',')

	next(repositories) # cabeçalho
	# repository_id,name,description,programming_language_id,url,create_date,end_date,duration_days,number_add_lines,number_del_lines,number_commits,number_commiters

	for row in repositories:
		rep_id = int(row[0])
		prog_lang_id = int(row[3])
		number_commiters = int(row[11])

		# inclui no dict cada repositório, o id da sua linguagem e o número de commiters
		rep_dict_language[rep_id] = [prog_lang_id, number_commiters]
r.close()
print("Finished read repository.csv")

# lê informações da rede realizando o cálculo da métrica
JCSR_metric = {}

print("Reading developers_social_network.csv...")
with open('../DataSet/developers_social_network.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,begin_contribution_date,end_contribution_date,contribution_days,number_add_lines,number_del_lines,number_commits

	for row in data:
		rep_id = int(row[0])

		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		total_JCSR = 0.0

		prog_lang_id = rep_dict_language[rep_id][0]
			
		# calcula JCSR para o par
		JCSR = 2 / rep_dict_language[rep_id][1]

		# cria um dict com cada par de desenvolvedores e o valor da métrica JCSR para eles
		# key = (programming_language_id, dev1, dev2) values = JCSR_metric_value
		if (prog_lang_id, dev_1_id, dev_2_id) in JCSR_metric:
			total_JCSR = JCSR_metric[prog_lang_id, dev_1_id, dev_2_id] + JCSR
			JCSR_metric[prog_lang_id, dev_1_id, dev_2_id] = total_JCSR
		else:
			JCSR_metric[prog_lang_id, dev_1_id, dev_2_id] = JCSR
r.close()

# ordena dict da métrica
print("Sorting JCSR metric dict...")
JCSR = collections.OrderedDict(sorted(JCSR_metric.items()))

# escreve todos os dados da métrica no arquivo final
print("Writing JCSR.csv...")
with open('../Files/JCSR.csv', 'w') as w:
	metric_file = csv.writer(w, delimiter=',')

	# escreve cabeçalho
	metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "JCSR"])

	# a soma dos valores da métrica são divididos pelo número de repositórios compartilhados entre os desenvolvedores (SR)
	for row in JCSR:
		metric_file.writerow([row[0], row[1], row[2], JCSR[row]/SR_metric[row]])
w.close()