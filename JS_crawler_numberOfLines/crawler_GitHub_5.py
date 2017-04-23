import requests, csv
from bs4 import BeautifulSoup
import re

count = 52000;
with open('../Files/JS_vector_url_commits_projects.csv', 'r') as r:
	data = csv.reader(r, delimiter=',')

	with open('../Files/JS_number_of_lines_5.csv', 'w') as w:
		writeit = csv.writer(w, delimiter=',') 
	
		for row in data:
			if(int(row[5]) > 8214133): #começa a coleta a partir do commit_id > 8214133
				user_login = row[3]
				project_name = row[1]
				commit_sha = row[6]
				url = "https://github.com/"+ user_login + "/" + project_name + "/commit/" + commit_sha
				r = requests.get(url)
				status = r.status_code

				if(status == 200):
					plain_text = r.text 

					soup = BeautifulSoup (plain_text, "html.parser")
					add = -1
					dell = -1
					for div in soup.findAll('div', {'class': 'toc-diff-stats'}):
					    additions = div.find('strong').text
					    deletions = div.find('strong').find_next_sibling().text
					    for a in re.findall(r'\d+', additions): add = a
					    for d in re.findall(r'\d+', deletions): dell = d
					print (url, add, dell)
					#Header: project_id, owner_id, commit_id, author_id, url, add, dell
					writeit.writerow([row[0], row[2], row[5], row[7], url, add, dell])	
				else:
					count +=1
					print (count)
	w.close()
r.close()