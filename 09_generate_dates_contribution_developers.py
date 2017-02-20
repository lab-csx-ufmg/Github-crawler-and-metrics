# script para geração das informações de datas e tempo de contribuição entre pares de usuários

# cabeçalho do arquivo gerado ((language)_dates_contribution_per_developers.csv): 
# 0 - repository_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - begin_contribution_date
# 4 - end_contribution_date
# 5 - contribution_days

from datetime import datetime
import sys, csv, operator

programming_language = sys.argv[1]

# ordenação da lista por repositório de desenvolvedor
def single_order(c):
	return (c[0], c[1])

# funçao de permutaçao dos usuarios por repositório
def permute(repository_id, list_users):
	# para cada conjunto de desenvolvedores, calcula valores dois a dois
	with open('Files/%s_dates_contribution_per_developers.csv' % (programming_language), 'a') as a:
		permute_file = csv.writer(a, delimiter=',')
		
		for i in list_users:
			for j in list_users:
				if i < j:
					if commits_with_dates[repository_id, i] > commits_with_dates[repository_id, j]:
						begin_contribution_date = commits_with_dates[repository_id, i]
					else:
						begin_contribution_date = commits_with_dates[repository_id, j]
					
					end_contribution_date = repository_dates[repository_id][1]
					contribution_days = (end_contribution_date - begin_contribution_date).days
					
					permute_file.writerow([repository_id, i, j, begin_contribution_date.strftime('%Y-%m-%d'), end_contribution_date.strftime('%Y-%m-%d'), contribution_days])
	a.close()

# cria lista com repositórios, usuários e a primeira data de commit do usuário
commits_str = {}
repositories_users = []

print("Reading commits_filtered_with_dates file with min commit data...")
with open('Files/%s_commits_filtered_with_dates.csv' %(programming_language), 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,author_id,sum_line_add,sum_line_del,count_commits

	for row in data:
		rep_id = int(row[0])
		dev_id = int(row[1])
		commit_id = int(row[2])
		create_date = row[3]
		
		if (rep_id, dev_id) in commits_str:
			if create_date != "0000-00-00":
				if commits_str[rep_id, dev_id] == "0000-00-00" or commits_str[rep_id, dev_id] > create_date:
					commits_str[rep_id, dev_id] = create_date	
		else:
			commits_str[rep_id, dev_id] = create_date
			repositories_users.append([rep_id, dev_id])
r.close()

# ordena lista de repositórios que será utilizada para permutação
usr_rep_list = sorted(repositories_users, key=single_order)

# cria dict de repositórios com datas iniciais e finais
repository_dates = {}

print("Reading repository_without_counts file...")
with open('Files/repository_without_counts.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,name,description,programming_language_id,url,create_date,end_date,duration_days
	
	for row in data:
		rep_id = int(row[0])
		create_date_str = row[5]
		end_date_str = row[6]

		create_date = datetime.strptime(create_date_str, '%Y-%m-%d')
		end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
		
		repository_dates[rep_id] = [create_date, end_date]
r.close()

# percorre dict de usuários e altera datas para tipo date
# se a data de algum dev for inválida, utiliza data inicial do repositório
commits_with_dates = {}

print("Validating commit dates...")
for commit in commits_str:
	if commits_str[commit] == "0000-00-00":
		rep_id = commit[0]
		commits_with_dates[commit] = repository_dates[rep_id][0]
	else:
		commits_with_dates[commit] = datetime.strptime(commits_str[commit], '%Y-%m-%d')

# percorre lista de projetos para realizar a permutacao
list_permute = []
last_repository = usr_rep_list[0][0] # primeiro projeto do arquivo

with open('Files/%s_dates_contribution_per_developers.csv' % (programming_language), 'w') as w:
		permute_file = csv.writer(w, delimiter=',')
		# cabeçalho
		permute_file.writerow(["repository_id", "developer_id_1", "developer_id_2", "begin_contribution_date", "end_contribution_date", "contribution_days"])
w.close()

print("Permuting developers per projects with dates...")
for row in usr_rep_list:
	rep_id = row[0]

	if rep_id == last_repository:
		list_permute.append(row[1])
	else:
		# permuta lista do last_repository
		permute(last_repository, list_permute)

		# limpa lista para próximo projeto
		list_permute = []
		list_permute.append(row[1])

	# atualiza last_repository
	last_repository = rep_id

# permuta lista do último projeto
permute(last_repository, list_permute)