# script para geração da métrica JWCOSR - Jointly Developers Weighted Commit to Share Repositories

# será gerado um arquivo contendo os valores da métrica por par de usuários
# adicionalmente, será gerado um segundo arquivo com todas as opções de cálculo disponíveis
# o arquivo gerado para a métrica SR é utilizado no cálculo da NL

# cabeçalho do arquivo gerado (NL.csv):
# 0 - programming_language_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - NL (NL_mod)

# cabeçalho do arquivo gerado (NL_all_options.csv):
# 0 - programming_language_id
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - NL_add
# 4 - NL_sum
# 5 - NL_dif
# 6 - NL_mods

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
		add_lines_rep = int(row[8])
		del_lines_rep = int(row[9])

		# inclui no dict cada repositório, o id da sua linguagem e as quantidades de linhas para a métrica
		sum_lines_rep = add_lines_rep + del_lines_rep
		dif_lines_rep = max(add_lines_rep - del_lines_rep, 0)
		mod_lines_rep = abs(add_lines_rep - del_lines_rep)
		
		rep_dict_language[rep_id] = [prog_lang_id, add_lines_rep, sum_lines_rep, dif_lines_rep, mod_lines_rep]
r.close()
print("Finished read repository.csv")

# lê informações da rede realizando os cálculos para a métrica
NL_metric = {}

print("Reading developers_social_network.csv...")
with open('../DataSet/developers_social_network.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	next(data) # cabeçalho
	# repository_id,developer_id_1,developer_id_2,begin_contribution_date,end_contribution_date,contribution_days,number_add_lines,number_del_lines,number_commits

	for row in data:
		rep_id = int(row[0])

		dev_1_id = int(row[1])
		dev_2_id = int(row[2])
		add_lines = int(row[6])
		del_lines = int(row[7])
		
		sum_lines = add_lines + del_lines
		dif_lines = max(add_lines - del_lines, 0)
		mod_lines = abs(add_lines - del_lines)

		prog_lang_id = rep_dict_language[rep_id][0]

		# recalcula utilizando a divisão pelas quantidades do repositório
		add_lines = 0 if rep_dict_language[rep_id][1] == 0 else (add_lines / rep_dict_language[rep_id][1])
		sum_lines = 0 if rep_dict_language[rep_id][2] == 0 else (sum_lines / rep_dict_language[rep_id][2])
		dif_lines = 0 if rep_dict_language[rep_id][3] == 0 else (dif_lines / rep_dict_language[rep_id][3])
		mod_lines = 0 if rep_dict_language[rep_id][4] == 0 else (mod_lines / rep_dict_language[rep_id][4])

		# normaliza valores menores que zero
		add_lines = 0 if add_lines < 0 else add_lines
		sum_lines = 0 if sum_lines < 0 else sum_lines
		dif_lines = 0 if dif_lines < 0 else dif_lines
		mod_lines = 0 if mod_lines < 0 else mod_lines
			
		# cria um dict com cada par de desenvolvedores e o valor dos cálculos para eles
		# key = (programming_language_id, dev1, dev2) values = add_lines, sum_lines, dif_lines, mod_lines
		if (prog_lang_id, dev_1_id, dev_2_id) in NL_metric:
			total_add_lines = NL_metric[prog_lang_id, dev_1_id, dev_2_id][0] + add_lines
			total_sum_lines = NL_metric[prog_lang_id, dev_1_id, dev_2_id][1] + sum_lines
			total_dif_lines = NL_metric[prog_lang_id, dev_1_id, dev_2_id][2] + dif_lines
			total_mod_lines = NL_metric[prog_lang_id, dev_1_id, dev_2_id][3] + mod_lines

			NL_metric[prog_lang_id, dev_1_id, dev_2_id] = [total_add_lines, total_sum_lines, total_dif_lines, total_mod_lines]
		else:
			NL_metric[prog_lang_id, dev_1_id, dev_2_id] = [add_lines, sum_lines, dif_lines, mod_lines]
r.close()

# ordena dict da métrica
print("Sorting NL metric dict...")
NL = collections.OrderedDict(sorted(NL_metric.items()))

# escreve todos os dados da métrica no arquivo final com métrica única
print("Writing NL.csv...")
with open('../Files/NL.csv', 'w') as w:
	metric_file = csv.writer(w, delimiter=',')

	# escreve cabeçalho
	metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "NL"])

	# a soma dos valores da métrica são divididos pelo número de repositórios compartilhados entre os desenvolvedores (SR)
	for row in NL:
		metric_file.writerow([row[0], row[1], row[2], NL[row][3]/SR_metric[row]])
w.close()

# escreve todos os dados da métrica no arquivo final com todas as opções
print("Writing NL_all_options.csv...")
with open('../Files/NL_all_options.csv', 'w') as w:
	metric_file = csv.writer(w, delimiter=',')

	# escreve cabeçalho
	metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "NL_add", "NL_sum", "NL_dif", "NL_mod"])

	# a soma dos valores da métrica são divididos pelo número de repositórios compartilhados entre os desenvolvedores (SR)
	for row in NL:
		metric_file.writerow([row[0], row[1], row[2], NL[row][0]/SR_metric[row], NL[row][1]/SR_metric[row], NL[row][2]/SR_metric[row], NL[row][3]/SR_metric[row]])
w.close()