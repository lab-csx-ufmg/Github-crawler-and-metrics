# script para geração da métrica JCOSR - Jointly Developers Commits to Shared Repositories

# será gerado um arquivo contendo os valores da métrica por par de usuários
# o arquivo gerado para a métrica SR é utilizado no cálculo da JCOSR

# cabeçalho da arquivo gerado (JCOSR.csv):
# 0 - programming_language_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - JCOSR

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

# cria dict com os repositórios da rede com sua linguagem e sua quantidade de commits
rep_dict_language = {}

print("Reading repository.csv...")
with open('../DataSet/repository.csv', 'r') as r:
	repositories = csv.reader(r, delimiter=',')

	next(repositories) # cabeçalho
	# repository_id,name,description,programming_language_id,url,create_date,end_date,duration_days,number_add_lines,number_del_lines,number_commits,number_commiters

	for row in repositories:
		rep_id = int(row[0])
		prog_lang_id = int(row[3])
		number_commits = int(row[10])

		# inclui no dict cada repositório, o id da sua linguagem e o número de commits
		rep_dict_language[rep_id] = [prog_lang_id, number_commits]
r.close()
print("Finished read repository.csv")

# lê informações da rede realizando o cálculo da métrica
JCOSR_metric = {}

print("Reading developers_social_network.csv...")
with open('../DataSet/developers_social_network.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,begin_contribution_date,end_contribution_date,contribution_days,number_add_lines,number_del_lines,number_commits

	for row in data:
		rep_id = int(row[0])

		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		num_commits = int(row[8])
		total_JCOSR = 0.0

		prog_lang_id = rep_dict_language[rep_id][0]
			
		# calcula JCOSR para o par
		JCOSR = num_commits / rep_dict_language[rep_id][1]

		# cria um dict com cada par de desenvolvedores e o valor da métrica JCOSR para eles
		# key = (programming_language_id, dev1, dev2) values = JCOSR_metric_value
		if (prog_lang_id, dev_1_id, dev_2_id) in JCOSR_metric:
			total_JCOSR = JCOSR_metric[prog_lang_id, dev_1_id, dev_2_id] + JCOSR
			JCOSR_metric[prog_lang_id, dev_1_id, dev_2_id] = total_JCOSR
		else:
			JCOSR_metric[prog_lang_id, dev_1_id, dev_2_id] = JCOSR
r.close()

# ordena dict da métrica
print("Sorting JCOSR metric dict...")
JCOSR = collections.OrderedDict(sorted(JCOSR_metric.items()))

# escreve todos os dados da métrica no arquivo final 
print("Writing JCOSR.csv...")
with open('../Files/JCOSR.csv', 'w') as w:
	metric_file = csv.writer(w, delimiter=',')

	# escreve cabeçalho
	metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "JCOSR"])

	# a soma dos valores da métrica são divididos pelo número de repositórios compartilhados entre os desenvolvedores (SR)
	for row in JCOSR:
		metric_file.writerow([row[0], row[1], row[2], JCOSR[row]/SR_metric[row]])
w.close()