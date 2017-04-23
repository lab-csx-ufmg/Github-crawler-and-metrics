# script para geração da métrica SR - Shared Repositories

# será gerado um arquivo contendo os valores da métrica por par de usuários

# cabeçalho da arquivo gerado (SR.csv): 
# 0 - programming_language_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - SR

import sys, csv, operator, collections

# cria dict com os repositórios e suas linguagens
rep_dict_language = {}

print("Reading repository.csv...")
with open('../DataSet/repository.csv', 'r') as r:
	repositories = csv.reader(r, delimiter=',')

	next(repositories) # cabeçalho
	# repository_id,name,description,programming_language_id,url,create_date,end_date,duration_days,number_add_lines,number_del_lines,number_commits,number_commiters

	for row in repositories:
		rep_id = int(row[0])
		prog_lang_id = int(row[3])

		# inclui no dict cada repositório e o id da sua linguagem
		rep_dict_language[rep_id] = prog_lang_id
r.close()
print("Finished read repository.csv")

# lê informações da rede realizando o cálculo da métrica
SR_metric = {}

print("Reading developers_social_network.csv...")
with open('../DataSet/developers_social_network.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,begin_contribution_date,end_contribution_date,contribution_days,number_add_lines,number_del_lines,number_commits

	for row in data:
		rep_id = int(row[0])

		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		total_SR = 0

		prog_lang_id = rep_dict_language[rep_id]

		# cria um dict com cada par de desenvolvedores e o valor da métrica SR para eles
		# key = (programming_language_id, dev1, dev2) values = SR_metric_value
		if (prog_lang_id, dev_1_id, dev_2_id) in SR_metric:
			total_SR = SR_metric[prog_lang_id, dev_1_id, dev_2_id] + 1
			SR_metric[prog_lang_id, dev_1_id, dev_2_id] = total_SR
		else:
			SR_metric[prog_lang_id, dev_1_id, dev_2_id] = 1
r.close()

# ordena dict da métrica
print("Sorting SR metric dict...")
SR = collections.OrderedDict(sorted(SR_metric.items()))

# escreve todos os dados da métrica no arquivo final
print("Writing SR.csv...")
with open('../Files/SR.csv', 'w') as w:
	metric_file = csv.writer(w, delimiter=',')

	# escreve cabeçalho
	metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "SR"])

	for row in SR:
		metric_file.writerow([row[0], row[1], row[2], SR[row]])
w.close()