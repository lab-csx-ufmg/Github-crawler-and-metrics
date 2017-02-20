# script para geração da base da network
# para isso, serão unidos os valores calculados pelos scripts 08 e 09

# será gerado um arquivo contendo os dados da rede para cada par de desenvolvedores num repositório

# cabeçalho da arquivo gerado (developers_social_network.csv): 
# 0 - repository_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - begin_contribution_date
# 4 - end_contribution_date
# 5 - contribution_days
# 6 - number_add_lines
# 7 - number_del_lines
# 8 - number_commits

import sys, csv, operator, collections

programming_language = sys.argv[1]

# cria dict com os dados da rede
dev_social_network = {}

# lê arquivo com datas e contribuições por par de desenvolvedores num repositorio
print("Reading %s_dates_contribution_per_developers.csv..." %(programming_language))
with open('Files/%s_dates_contribution_per_developers.csv' %(programming_language), 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,begin_contribution_date,end_contribution_date,contribution_days

	for row in data:
		rep_id = int(row[0])
		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		begin_contrib = row[3]
		end_contrib = row[4]
		contrib_days = int(row[5])

		# cria um dict com datas e contribuição e espaços em branco para inclusão de novos itens
		# key = (repository_id, dev1, dev2) values = [begin_contrib, end_contrib, contrib_days, add_lines, del_lines, num_commits]
		if (rep_id, dev_1_id, dev_2_id) in dev_social_network:
			print('ERRO - duplicated repository and developers on file! -', repository_id, dev_1_id, dev_2_id)
		else:
			dev_social_network[rep_id, dev_1_id, dev_2_id] = [begin_contrib, end_contrib, contrib_days, 0, 0, 0]
r.close()

# lê arquivo com número de linhas adicionadas, deletadas e commits por repositório
print("Reading %s_total_add_del_commits_per_developers.csv..." %(programming_language))
with open('Files/%s_total_add_del_commits_per_developers.csv' %(programming_language), 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,number_add_lines,number_del_lines,number_commits

	for row in data:
		rep_id = int(row[0])
		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		add_lines = int(row[3])
		del_lines = int(row[4])
		commits = int(row[5])

		# complementa o dict da rede
		# key = (repository_id, dev1, dev2) values = [begin_contrib, end_contrib, contrib_days, add_lines, del_lines, num_commits]
		if (rep_id, dev_1_id, dev_2_id) in dev_social_network:
			dev_social_network[rep_id, dev_1_id, dev_2_id][3] = add_lines
			dev_social_network[rep_id, dev_1_id, dev_2_id][4] = del_lines
			dev_social_network[rep_id, dev_1_id, dev_2_id][5] = commits
		else:
			print('ERRO - duplicated repository and developers on file! -', repository_id, dev_1_id, dev_2_id)
r.close()

# tenta abrir arquivo para verificar existência
# se não existir, cria arquivo com cabeçalho
try:
	with open('DataSet/developers_social_network.csv', 'r') as r:
		network_file = csv.reader(r, delimiter=',')
	r.close()
except FileNotFoundError:
	with open('DataSet/developers_social_network.csv', 'w') as w:
		network_file = csv.writer(w, delimiter=',')

		# cabeçalho do arquivo
		network_file.writerow(["repository_id", "developer_id_1", "developer_id_2", "begin_contribution_date", "end_contribution_date", "contribution_days", "number_add_lines", "number_del_lines", "number_commits"])
	w.close()

# ordena dict da network
print("Sorting network dict...")
network_sort = collections.OrderedDict(sorted(dev_social_network.items()))

# escreve todos os dados da network no arquivo final
print("Writing developers_social_network.csv...")
# será utilizado 'a' para abertura do arquivo a fim de unir mais de uma linguagem de programação
with open('DataSet/developers_social_network.csv', 'a') as a:
	network_file = csv.writer(a, delimiter=',')

	print("Writing developers_social_network file for", programming_language)

	for row in network_sort:
		network_file.writerow([row[0], row[1], row[2], network_sort[row][0], network_sort[row][1], network_sort[row][2], network_sort[row][3], network_sort[row][4], network_sort[row][5]])
a.close()