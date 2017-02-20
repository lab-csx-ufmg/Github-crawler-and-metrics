# script para geração da base de usuários contendo seus principais dados
# para isso, serão levados em consideração todos os usuários da rede independente de linguagens de programação

# cabeçalho da arquivo gerado (user.csv): 
# 0 - user_id
# 1 - name
# 2 - login
# 3 - company
# 4 - location
# 5 - email
# 6 - type
# 7 - fake
# 8 - deleted

from datetime import datetime
import csv

# percorre arquivo de usuário escrevendo o novo arquivo para o data set
print("Reading users.csv and writing user.csv...")
with open('DataSet/user.csv', 'w') as w:
	users_file = csv.writer(w, delimiter=',')
	users_file.writerow(["user_id", "name", "login", "company", "location", "email", "type", "fake", "deleted"])

	with open('Files/users.csv', 'r') as r:
		data = csv.reader(r, delimiter=',')
		
		for row in data:
			user_id = int(row[0])
			login = row[1]
			name = row[2]
			company = row[3]
			location = row[4]
			email = row[5]
			created_at = row[6][:10]
			usr_type = row[7]
			fake = int(row[8])
			deleted = int(row[9])

			# limpa campos com valor \\N
			if name == '\\N':
				name = ''
			if company == '\\N':
				company = ''
			if location == '\\N':
				location = ''
			if email == '\\N':
				email = ''
	
			# escreve linha no arquivo de usuários	
			users_file.writerow([user_id, name, login, company, location, email, created_at, usr_type, fake, deleted])			
	r.close()
w.close()
print("Finished write user.csv")