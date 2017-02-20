# script para união das informações dos repositórios e criação do arquivo único repository.csv do data set

# cabeçalho do arquivo gerado (repository.csv): 
# 0 - repository_id
# 1 - name
# 2 - description
# 3 - programming_language_id
# 4 - url
# 5 - create_date
# 6 - end_date
# 7 - duration_days
# 8 - number_add_lines
# 9 - number_del_lines
# 10 - number_commits
# 11 - number_commiters

import sys, csv, operator, collections

# a lista de linguagens de programação será recebida via linha de comando
programming_languages = sys.argv[1:]

# leitura do arquivo inicial de repositórios que contém todos eles (inclusive repositórios sem commits)
with open('Files/repository_without_counts.csv', 'r') as csvfile:
		data = csv.reader(csvfile, delimiter=',')
		
		next(data) # cabeçalho
		# repository_id,name,description,programming_language_id,url,create_date,end_date,duration_days

		print("Reading repository_without_counts file...")
		repositories = {}

		for row in data:
			repository_id = int(row[0])
			name = row[1]
			description = row[2]
			programming_language_id = int(row[3])
			url = row[4]
			create_date = row[5]
			end_date = row[6]
			duration_days = int(row[7])

			# cria um dict com repositories e espaços em branco para inclusão de novos itens
			# key = repository_id, values = [name, description, prog_lang_id, url, create_date, end_date, durantion_days, number_add_lines, number_del_lines, number_commits, number_commiters]
			if repository_id in repositories:
				print('ERRO - duplicated repository on file! -', repository_id)
			else:
				repositories[repository_id] = [name, description, programming_language_id, url, create_date, end_date, duration_days, 0, 0, 0, 0]
csvfile.close()	

# lê arquivos com detalhes dos projetos das linguagens da linha de comando para agregar informações
for i in range(0, len(programming_languages)):
	with open('Files/%s_total_add_del_commits_per_repository.csv' % (programming_languages[i]), 'r') as csvfile:
			data = csv.reader(csvfile, delimiter=',')
			
			next(data) # cabeçalho
			# repository_id,number_add_lines,number_del_lines,number_commits,number_commiters

			print("Reading %s_total_add_del_commits_per_repository.csv..." % (programming_languages[i]))
			
			# para cada linha nestes arquivos, complementa informações existentes
			for row in data:
				repository_id = int(row[0])
				number_add_lines = int(row[1])
				number_del_lines = int(row[2])
				number_commits = int(row[3])
				number_commiters = int(row[4])

				# complementa o dict de repositories
				# key = repository_id, values = [name, description, prog_lang_id, url, create_date, end_date, durantion_days, number_add_lines, number_del_lines, number_commits, number_commiters]
				if repository_id in repositories:
					repositories[repository_id][7] = number_add_lines
					repositories[repository_id][8] = number_del_lines
					repositories[repository_id][9] = number_commits
					repositories[repository_id][10] = number_commiters
				else:
					print('ERRO - duplicated repository on file! -', programming_languages[i], "-", repository_id)
	csvfile.close()

# ordena dict de repositories completo
print("Sorting complete repository dict...")
reps_sort = collections.OrderedDict(sorted(repositories.items()))

with open('DataSet/repository.csv', 'w') as f:
	writeit = csv.writer(f, delimiter=',')
	
	# cabeçalho
	writeit.writerow(["repository_id", "name", "description", "programming_language_id", "url", "create_date", "end_date", "duration_days", "number_add_lines", "number_del_lines", "number_commits", "number_commiters"])
	print("Writing repository file...")

	for rep_id in reps_sort:
		name = reps_sort[rep_id][0]
		description = reps_sort[rep_id][1]
		programming_language_id = reps_sort[rep_id][2]
		url = reps_sort[rep_id][3]
		create_date = reps_sort[rep_id][4]
		end_date = reps_sort[rep_id][5]
		duration_days = reps_sort[rep_id][6]
		number_add_lines = reps_sort[rep_id][7]
		number_del_lines = reps_sort[rep_id][8]
		number_commits = reps_sort[rep_id][9]
		number_commiters = reps_sort[rep_id][10]

		writeit.writerow([rep_id, name, description, programming_language_id, url, create_date, end_date, duration_days, number_add_lines, number_del_lines, number_commits, number_commiters])
f.close()