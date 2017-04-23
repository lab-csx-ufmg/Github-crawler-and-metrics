# script para geração das redes que serão utilizadas para os cálculos das métricas topológicas 

# serão gerados arquivos contendo os pares de usuários para cada linguagem da rede

# cabeçalho da arquivo gerado ((language)_topological_network.csv):
# 0 - developer_id_1
# 1 - developer_id_2

import sys, csv, operator, collections

# cria dict com todos os acrônimos das linguagens de programação (apenas JavaScript e Ruby)
prog_languages = {}

print("Reading programming_language.csv...")
with open('../DataSet/programming_language.csv', 'r') as r:
	prog_lang = csv.reader(r, delimiter=',')

	next(prog_lang) # cabeçalho
	# programming_language_id,name,acronym
	
	for row in prog_lang:
		programming_language_id = int(row[0])
		programming_language_acronym = row[2].upper()
		
		if programming_language_acronym in ['JS', 'RB']:
			# inclui linguagem no dict
			prog_languages[programming_language_id] = programming_language_acronym
r.close()
print("Finished read programming_language.csv")

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

# lê informações das redes e cria dict com os pares de desenvolvedores por linguagens
t_network = {}

print("Reading developers_social_network.csv...")
with open('../DataSet/developers_social_network.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,begin_contribution_date,end_contribution_date,contribution_days,number_add_lines,number_del_lines,number_commits

	for row in data:
		rep_id = int(row[0])

		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		
		prog_lang_id = rep_dict_language[rep_id]
			
		# inclui o par na rede por linguagem (caso não exista)
		if (prog_lang_id, dev_1_id, dev_2_id) not in t_network:
			t_network[prog_lang_id, dev_1_id, dev_2_id] = 1
r.close()
print("Finished read developers_social_network.csv")

# ordena dict da métrica
print("Sorting network topological metrics dict...")
topological_network = collections.OrderedDict(sorted(t_network.items()))

# escreve todos os pares da rede em arquivos distintos por linguagem
for prog_lang_id in prog_languages:
	print("Writing %s_topological_network.csv..." % (prog_languages[prog_lang_id]))
	with open('../Files/%s_topological_network.csv' % (prog_languages[prog_lang_id]), 'w') as w:
		network_file = csv.writer(w, delimiter=',')

		# escreve pares da rede apenas para a linguagem atual
		for row in topological_network:
			if row[0] == prog_lang_id:
				network_file.writerow([row[1], row[2]])
	w.close()