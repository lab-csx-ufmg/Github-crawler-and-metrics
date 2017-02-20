# script para geração da base de repositórios contendo suas datas iniciais e finais
# para isso, devem ser levados em consideração os repositórios dos arquivos JS_projects.csv e RB_projects.csv (a linguagem será recebida via linha de comando)

# será gerado um arquivo contendo os dados do repositório sem os counts de commits, add_lines e del_lines (dados serão acrescentados por outro script para a base final)

# cabeçalho da arquivo gerado (repository_without_counts.csv): 
# 0 - repository_id
# 1 - name
# 2 - description
# 3 - programming_language_id
# 4 - url
# 5 - create_date
# 6 - end_date
# 7 - duration_days

from datetime import datetime
import csv
import sys

programming_language = sys.argv[1]

# cria dict com todas as linguagens de programação utilizando o nome como dado
prog_languages = {}

print("Reading programming_language.csv...")
with open('DataSet/programming_language.csv', 'r') as r:
	prog_lang = csv.reader(r, delimiter=',')
	next(prog_lang) # cabeçalho
	
	for row in prog_lang:
		programming_language_id = int(row[0])
		programming_language_name = row[1].upper()
		
		# inclui linguagem no dict
		prog_languages[programming_language_name] = programming_language_id
r.close()
print("Finished read programming_language.csv")

# cria dict com os repositórios
repositories = {}

print("Reading %s_projects.csv..." %(programming_language))
with open('Files/%s_projects.csv' %(programming_language), 'r') as r:
	data = csv.reader(r, delimiter=',')
	
	for row in data:
		rep_id = int(row[0])
		rep_url = row[1]
		owner_id = int(row[2])
		rep_name = row[3]
		rep_desc = row[4]
		rep_language = row[5].upper()
		rep_create_date = row[6][:10]
	
		rep_list = [rep_name, rep_desc, prog_languages[rep_language], rep_url, rep_create_date, rep_create_date, 0]
		repositories[rep_id] = rep_list
r.close()
print("Finished read %s_projects.csv..." %(programming_language))

# percorre arquivo com os commits para validar data inicial menor que o primeiro commit
# em conjunto, também define data final do projeto
print("Start validating dates...")
with open('Files/%s_commits_filtered_with_dates.csv' %(programming_language), 'r') as r:
	data = csv.reader(r, delimiter=',')
	
	for row in data:
		rep_id = int(row[0])
		create_date_commit = row[3]
		
		# não realiza alteração se data não for válida
		if create_date_commit != '0000-00-00':
			# avalia data inicial			
			if repositories[rep_id][4] > create_date_commit:
				print("Change project", rep_id, "begin date", repositories[rep_id][4], "to", create_date_commit)
				repositories[rep_id][4] = create_date_commit
			
			# avalia data final
			if repositories[rep_id][5] < create_date_commit:
				print("Change project", rep_id, "end date", repositories[rep_id][5], "to", create_date_commit)
				repositories[rep_id][5] = create_date_commit
r.close()
print("Finished validating dates")

# tenta abrir arquivo para verificar existência
# se não existir, cria arquivo com cabeçalho
try:
	with open('Files/repository_without_counts.csv', 'r') as r:
		repositories_file = csv.reader(r, delimiter=',')
	r.close()
except FileNotFoundError:
	with open('Files/repository_without_counts.csv', 'w') as w:
		repositories_file = csv.writer(w, delimiter=',')

		# cabeçalho do arquivo
		repositories_file.writerow(["repository_id", "name", "description", "programming_language_id", "url", "create_date", "end_date", "duration_days"])
	w.close()

# calcula duração dos repositórios em dias e escreve no arquivo final
print("Writing repository_without_counts.csv...")
# será utilizado 'a' para abertura do arquivo a fim de unir mais de uma linguagem de programação
with open('Files/repository_without_counts.csv', 'a') as a:
	repositories_file = csv.writer(a, delimiter=',')

	for rep in repositories:
		begin_date = datetime.strptime(repositories[rep][4], '%Y-%m-%d')
		end_date = datetime.strptime(repositories[rep][5], '%Y-%m-%d')
		duration_days = end_date - begin_date

		repositories[rep][6] = duration_days.days

		# se a duração for menor que zero...
		if repositories[rep][6] < 0:
			print("Check dates repository", rep, "-", repositories[rep])
		
		repositories_file.writerow([rep, repositories[rep][0], repositories[rep][1], repositories[rep][2], repositories[rep][3], repositories[rep][4], repositories[rep][5], repositories[rep][6]])
a.close()
print("Finished write repository_without_counts.csv")
