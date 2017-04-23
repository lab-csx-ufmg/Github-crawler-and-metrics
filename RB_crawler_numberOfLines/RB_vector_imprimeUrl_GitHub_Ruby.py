import sys, csv, operator

with open('../Files/RB_projects.csv', 'r') as projects_file:
	data = csv.reader(projects_file, delimiter=',')
	#projects = [0]*26036400 #ultimo project_id existente (26036399+1)
	projects = [0]*26036400
	for row in data:
		project_id = int(row[0])
		project_name = row[3]
		project_owner = int(row[2])
		projects[project_id] = [project_name,project_owner]
projects_file.close()

with open('../Files/users.csv', 'r') as users_file:
	data = csv.reader(users_file, delimiter=',')
	#users = [0]*9524037 #ultimo user_id existente (9524036+1)
	users = [0]*9524037
	for row in data:
		user_id = int(row[0])
		user_login = row[1]
		users[user_id] = user_login
users_file.close()			


commit_project_id=0

with open('../Files/commits.csv', 'r') as commits_file:
	data = csv.reader(commits_file, delimiter=',')
	with open('vector_url_commits_projects_Ruby.csv', 'a') as w:
		writeit = csv.writer(w, delimiter=',')
		for row in data:
			try: 
				commit_project_id = int(row[4])
				print (commit_project_id)
			except: 
				print (commit_project_id)
				commit_project_id = 0 #ignora os valores '//N' -> commit sem projeto
			if(projects[commit_project_id] != 0): #só os projetos de Ruby serão impressos
				project_owner_id = projects[commit_project_id][1]
				author_id = int(row[2])
				print (commit_project_id, projects[commit_project_id][0], project_owner_id, users[project_owner_id], row[5], row[0], row[1], author_id, users[author_id])
				#HEADER: project_id, project_name, project_owner_id, project_owner_login, date_commit, id_commit, sha_commit, author_commit_id, author_commit_login
				writeit.writerow([commit_project_id, projects[commit_project_id][0], project_owner_id, users[project_owner_id], row[5], row[0], row[1], author_id, users[author_id]])
	w.close()
commits_file.close()