# script para filtrar quais dos commits serão levados em consideração para o dataset (de acordo com a coleta do número de linhas)
# será gerada uma nova lista apenas com os commits que serão considerados por repositório para cada arquivo do crawler

# cabeçalho do arquivo gerado:
# 0 - project_id
# 1 - developer_id
# 2 - commit_id
# 3 - commit_date

# o script recebe a linguagem e a quantidade de arquivos number_of_lines

import csv
import sys

programming_language = sys.argv[1]
number_of_files = sys.argv[2]

for file_number in range(0, number_of_files):
	# cria lista de commits válidos para os repositórios (por arquivo _number_of_lines_X)
	with open('Files/%snumber_of_lines_%d.csv' %(programming_language, file_number), 'r') as r:
		valid_commits = []
		data = csv.reader(r, delimiter=',')
	
		# cabeçalho dos arquivos number_of_lines_X
		# 0 - project_id
		# 1 - owner_id
		# 2 - commit_id
		# 3 - author_id
		# 4 - url
		# 5 - add
		# 6 - dell
	
		for row in data:
			valid_commits.append(int(row[2])) # commit id
	r.close()
print("Finished commit list")

# utiliza lista criada para filtrar os commits permitidos e criar arquivo final
with open('Files/%s_commits_filtered_with_dates.csv' %(programming_language), 'w') as w:
	commits_final = csv.writer(w, delimiter=',')

	with open('Files/%s_vector_url_commits_projects.csv' %(programming_language), 'r') as r:
		data = csv.reader(r, delimiter=',')
	
		# cabeçalho do arquivo vector_url_commits_projects.csv
		# 0 - project_id
		# 1 - project_name
		# 2 - owner_id
		# 3 - owner_login
		# 4 - commit_date
		# 5 - commit_id
		# 6 - commit_sha
		# 7 - author_id
		# 8 - author_login
		
		for row in data:
			if int(row[5]) in valid_commits: # avalia existência do commit na lista permitida
				commits_final.writerow([row[0], row[7], row[5], row[4][:10]])
	r.close()
w.close()
print("Finished write final file")
