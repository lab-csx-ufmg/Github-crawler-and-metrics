# script para levantamento das demais informações de repositórios (número de linhas adicionadas, deletadas, commits e commiters)

# cabeçalho da arquivo gerado ((language)_total_add_del_commits_per_repository.csv): 
# 0 - repository_id
# 1 - number_add_lines
# 2 - number_del_lines
# 3 - number_commits
# 4 - number_commiters

import sys, csv, operator, collections

programming_language = sys.argv[1]

with open('Files/%s_sum_lines.csv' % (programming_language), 'r') as csvfile:
		data = csv.reader(csvfile, delimiter=',')
		next(data) # cabeçalho

		print("Reading sum_lines file...")
		repositories = {}

		for row in data:
			repository_id = int(row[0])
			user_id = int(row[1])
			add_lines = int(row[2])
			del_lines = int(row[3])
			commits = int(row[4])
			users_list = []

			# cria um dict com repositories e commits
			# o último elemento é uma lista com os commiters distintos por repositório
			# key = repository_id, values = [sum_lines_add, sum_lines_del, count_commits, [users_list]]
			if repository_id in repositories:
				sum_add_lines = repositories[repository_id][0] + add_lines
				sum_del_lines = repositories[repository_id][1] + del_lines
				sum_commits = repositories[repository_id][2] + commits

				# verifica se user já está na sublista
				users_list = repositories[repository_id][3]
				if user_id not in users_list:
					users_list.append(user_id)

				repositories[repository_id] = [sum_add_lines, sum_del_lines, sum_commits, users_list]
			else:
				users_list = [user_id]
				repositories[repository_id] = [add_lines, del_lines, commits, users_list]
csvfile.close()	

# ordena dict de repositories
print("Sorting repository dict...")
reps_sort = collections.OrderedDict(sorted(repositories.items()))

with open('Files/%s_total_add_del_commits_per_repository.csv' % (programming_language), 'w') as f:
	writeit = csv.writer(f, delimiter=',')
	
	# cabeçalho
	writeit.writerow(["repository_id", "number_add_lines", "number_del_lines", "number_commits", "number_commiters"])
	print("Writing total_add_del_commits_per_repository file...")

	for rep_id in reps_sort:
		number_add_lines = reps_sort[rep_id][0]
		number_del_lines = reps_sort[rep_id][1]
		number_commits = reps_sort[rep_id][2]
		number_commiters = len(reps_sort[rep_id][3])

		writeit.writerow([rep_id, number_add_lines, number_del_lines, number_commits, number_commiters])
f.close()