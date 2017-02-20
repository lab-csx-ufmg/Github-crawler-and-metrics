# script para geração da base de linguagens de programação do data set

# cabeçalho da arquivo gerado (programming_language.csv): 
# 0 - programming_language_id
# 1 - programming_language_name

import csv

print("Create programming languages list...")

programming_languages = []

# inicialmente, trabalharemos com JavaScript, Ruby e futuramente Java
programming_languages.append(["JavaScript", "JS"])
programming_languages.append(["Ruby", "RB"])
programming_languages.append(["Java", "J"])

print("Sort programming languages list...")

# ordena lista em ordem alfabética
programming_languages.sort()

print("Writing programing_language.csv...")
with open('DataSet/programming_language.csv', 'w') as w:
	prog_lang = csv.writer(w, delimiter=',')
	count_lang = 0
	
	# cabeçalho do arquivo
	prog_lang.writerow(["programming_language_id", "name", "acronym"])

	for language in programming_languages:
		prog_lang.writerow([count_lang, language[0], language[1]])
		count_lang += 1
w.close()
print("Finish write programing_language.csv")
