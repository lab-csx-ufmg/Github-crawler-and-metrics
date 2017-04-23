# script para geração da métrica PC - Previous Collaboration

# será gerado um arquivo contendo os valores da métrica por par de usuários
# o arquivo gerado para a métrica SR é utilizado no cálculo da PC

# cabeçalho do arquivo gerado (PSC.csv):
# 0 - programming_language_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - PSC

import sys, csv, operator, collections

# ordenação da lista por projeto, desenvolvedor e data do commit
def single_order(c):
	return (c[0], c[1], c[3])

# ordenação da lista por projeto e data do commit
def project_order(c):
	return (c[0], c[3])

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

# cria dict com os repositórios da rede
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

# cria lista com todos os commits de projetos para definir o primeiro commit por usuário
commits_no_order = []

for programing_language in ['JS', 'RB']:
	print("Reading %s_commits_filtered_with_dates.csv..." %(programming_language))
	with open('%s_commits_filtered_with_dates.csv' %(programming_language), 'r') as r:
		data = csv.reader(r, delimiter=',')
		
		for row in data:
			project_id = int(row[0])
			author_id = int(row[1])
			commit_id = int(row[2])
			create_date = row[3]
			
			commit_line = (project_id, author_id, commit_id, create_date)
			commits_no_order.append(commit_line)
			
			count_commits = count_commits + 1
			print(str(count_commits) + " - read commit " + row[2])
	r.close()
	print("Finished read %s_commits_filtered_with_dates.csv" %(programming_language))

print("Sorting commits with dates...")
commits = sorted(commits_no_order, key=single_order)
commits_no_order = [] # descarta lista não ordenada

# para cada commiter em um projeto distinto, considerar apenas a primeira linha (primeiro commit no projeto)

first_commits_no_order = []
last_project = 0
last_user = 0

print("Selecting first commit per user...")

count_commits = 0	

for commit in commits:
	# 0 - project_id
	# 1 - author_id
	# 2 - commit_id
	# 3 - create_date
				
	if last_project != commit[0] or (last_project == commit[0] and last_user != commit[1]):
		first_commits_no_order.append(commit)
		
		last_project = commit[0]
		last_user = commit[1]
		
	count_commits = count_commits + 1
	print(str(count_commits) + " - first commit " + str(commit[2]))

commits = [] # descarta lista completa de commits

print("Sorting commits with dates per user...")
first_commits_order = sorted(first_commits_no_order, key=project_order)
first_commits_no_order = [] # descarta lista não ordenada

PSC_user_order = {}

count_line = 0
last_project = 0
count_dev = 0
	
for first_commit in first_commits_order:
	if first_commit[0] != last_project:
		count_dev = 1
	else:
		count_dev = count_dev + 1
		if (first_commit[0], first_commit[1]) in PSC_user_order:
			print("Duplicated first commit user on project!")
		else:
			PSC_user_order[first_commit[0], first_commit[1]] = count_dev
		
	last_project = first_commit[0]
	
	count_line = count_line + 1
	
# lê informações da rede realizando os cálculos para a métrica
PSC_metric = {}

print("Reading developers_social_network.csv...")
with open('../DataSet/developers_social_network.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,begin_contribution_date,end_contribution_date,contribution_days,number_add_lines,number_del_lines,number_commits

	for row in data:
		rep_id = int(row[0])

		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		
		qtd_dev_1 = PSC_user_order[rep_id, dev_1_id] - 1
		qtd_dev_2 = PSC_user_order[rep_id, dev_2_id] - 1
		
		prog_lang_id = rep_dict_language[rep_id]

		# calcula métrica utilizando maior valor
		if qtd_dev_1 < qtd_dev_2:
			PSC_value = 1/qtd_dev_1
		else:
			PSC_value = 1/qtd_dev_2
			
		# cria um dict com cada par de desenvolvedores e o valor dos cálculos para eles
		# key = (programming_language_id, dev1, dev2) values = PSC_value
		if (prog_lang_id, dev_1_id, dev_2_id) in PSC_metric:
			total_PSC_value = PSC_metric[prog_lang_id, dev_1_id, dev_2_id] + PSC_value
			PSC_metric[prog_lang_id, dev_1_id, dev_2_id] = total_PSC_value
		else:
			PSC_metric[prog_lang_id, dev_1_id, dev_2_id] = PSC_value
r.close()

# ordena dict da métrica
print("Sorting PSC metric dict...")
PSC = collections.OrderedDict(sorted(PSC_metric.items()))

# escreve todos os dados da métrica no arquivo final com métrica única
print("Writing PSC.csv...")
with open('../Files/PSC.csv', 'w') as w:
	metric_file = csv.writer(w, delimiter=',')

	# escreve cabeçalho
	metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "PSC"])

	# a soma dos valores da métrica são divididos pelo número de repositórios compartilhados entre os desenvolvedores (SR)
	for row in NL:
		metric_file.writerow([row[0], row[1], row[2], PSC[row]/SR_metric[row]])
w.close()