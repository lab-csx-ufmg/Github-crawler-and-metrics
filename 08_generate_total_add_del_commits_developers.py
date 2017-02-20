# script para geração das informações de linhas adicionadas, deletadas e commits entre pares de usuários

# cabeçalho do arquivo gerado ((language)_total_add_del_commits_per_developers.csv): 
# 0 - repository_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - number_add_lines
# 4 - number_del_lines
# 5 - number_commits

import sys, csv, operator

programming_language = sys.argv[1]

# funçao de permutaçao dos usuarios por repositório
def permute(repository_id, list_users):
	# para cada conjunto de desenvolvedores, calcula valores dois a dois
	with open('Files/%s_total_add_del_commits_per_developers.csv' % (programming_language), 'a') as a:
		permute_file = csv.writer(a, delimiter=',')
		
		for i in list_users:
			for j in list_users:
				if i[0] < j[0]:
					number_add_lines = i[1] + j[1]
					number_del_lines = i[2] + j[2]
					number_commits = i[3] + j[3]
					
					permute_file.writerow([repository_id, i[0], j[0], number_add_lines, number_del_lines, number_commits])
	a.close()

# cria lista com projetos e usuários e os cálculos dos numeros de linha para cada user
usr_rep_list = []

print("Reading sum_lines list...")

with open('Files/%s_sum_lines.csv' % (programming_language), 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,author_id,sum_line_add,sum_line_del,count_commits

	for row in data:
		rep_id = int(row[0])
		dev_id = int(row[1])
		add = int(row[2])
		dell = int(row[3])
		commits = int(row[4])

		usr_rep_list.append([rep_id, dev_id, add, dell, commits])
r.close()

# percorre lista de projetos para realizar a permutacao
list_permute = []
last_repository = usr_rep_list[0][0] # primeiro projeto do arquivo

with open('Files/%s_total_add_del_commits_per_developers.csv' % (programming_language), 'w') as w:
		permute_file = csv.writer(w, delimiter=',')
		# cabeçalho
		permute_file.writerow(["repository_id", "developer_id_1", "developer_id_2", "number_add_lines", "number_del_lines", "number_commits"])
w.close()

print("Permuting developers per projects...")
for row in usr_rep_list:
	rep_id = row[0]

	if rep_id == last_repository:
		list_permute.append([row[1], row[2], row[3], row[4]])
	else:
		# permuta lista do last_repository
		permute(last_repository, list_permute)

		# limpa lista para próximo projeto
		list_permute = []
		list_permute.append([row[1], row[2], row[3], row[4]])

	# atualiza last_repository
	last_repository = rep_id

# permuta lista do último projeto
permute(last_repository, list_permute)