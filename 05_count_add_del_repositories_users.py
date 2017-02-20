# script para união dos arquivos criados pelo crawler e cálculo dos counts
# serão calculadas as quantidades de linhas adicionadas, deletadas e commits por usuário em cada repositório

# cabeçalho da arquivo gerado ((language)_sum_lines.csv): 
# 0 - repository_id
# 1 - author_id
# 2 - sum_line_add
# 3 - sum_line_del
# 4 - count_commits

import sys, csv, operator
import collections
import sys

# recupera a linguagem executada e a quantidade de arquivos da linha de comando
programming_language = sys.argv[1]
number_of_files = int(sys.argv[2])

line_users_projects = {}

# realiza a união dos arquivos number_of_lines com as contagens
def _merge_files(file_name, mydict):
	with open(file_name, 'r') as f1:
		data = csv.reader(f1, delimiter=',')

		print("Reading file", file_name, "...")

		for row in data:
			repository_id = int(row[0])
			author_id = int(row[3])
			line_add = int(row[5])
			line_del = int(row[6])
			n_commits = 1

			if((repository_id,author_id) in mydict):
				sum_line_add = mydict[(repository_id,author_id)][0] + line_add
				sum_line_del = mydict[(repository_id,author_id)][1] + line_del
				count_commits = mydict[(repository_id,author_id)][2] + 1 
				mydict[(repository_id,author_id)] = [sum_line_add, sum_line_del, count_commits]
			else:
				mydict[(repository_id,author_id)] = [line_add, line_del, n_commits]
	f1.close()

for i in range(0,number_of_files): # do arquivo 0 ao X 
	_merge_files('Files/%s_number_of_lines_%d.csv' % (programming_language, i),line_users_projects)

# ordena dict de commits
print("Sorting commits dict...")
od = collections.OrderedDict(sorted(line_users_projects.items()))

# impreime no arquivo final
print("Writing sum_lines file...")
with open('Files/%s_sum_lines.csv' % (programming_language), 'w') as w:
	writeit = csv.writer(w, delimiter=',')

	# cabeçalho
	writeit.writerow(["repository_id", "author_id", "sum_line_add", "sum_line_del", "count_commits"])

	for row in od:
		#HEADER: repository_id, author_id, sum_line_add, sum_line_del, count_commits
		writeit.writerow([row[0], row[1], od[row][0], od[row][1], od[row][2]])