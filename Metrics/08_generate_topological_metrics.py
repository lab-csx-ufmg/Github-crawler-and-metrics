# script para geração das métricas topológicas a partir das redes de usuários

# cabeçalho da arquivo gerado (topological_metrics.csv):
# 0 - programming_language
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - n_overlap
# 4 - a_adar
# 5 - p_att

import networkx as nx
import sys, csv, operator, collections

# cria arquivo que conterá as métricas topológicas e escreve cabeçalho
print("Writing header topological_metrics.csv...")
with open('../Files/topological_metrics.csv', 'w') as w:
	metrics_file = csv.writer(w, delimiter=',')
	
	# cabeçalho
	metrics_file.writerow(['programming_language_id', 'developer_id_1', 'developer_id_2', 'n_overlap', 'a_adar', 'p_att'])
w.close()

# cria dict com todos os acrônimos das linguagens de programação (apenas JavaScript e Ruby)
prog_languages = {}

print("Reading programming_language.csv...")
with open('../DataSet/programming_language.csv', 'r') as r:
	prog_lang = csv.reader(r, delimiter=',')

	next(prog_lang) # cabeçalho
	# programming_language_id,name,acronym
	
	for row in prog_lang:
		programming_language_id = int(row[0])
		programming_language_acronym = row[2].upper()
		
		if programming_language_acronym in ['JS', 'RB']:
			# inclui linguagem no dict
			prog_languages[programming_language_id] = programming_language_acronym
r.close()
print("Finished read programming_language.csv")

# realiza os cálculos das métricas topológicas quantas vezes forem as linguagens de programação consideradas
for prog_lang_id in prog_languages:
	print('Generating network for language', prog_languages[prog_lang_id])
	G = nx.read_weighted_edgelist('/Users/gabriela/Desktop/IC/artigo_parte2/MSR_DataShowcase/Files/%s_topological_network.csv' % (prog_languages[prog_lang_id]), delimiter=',', nodetype=int) 
	
	with open('../Files/%s_topological_network.csv' % (prog_languages[prog_lang_id]), 'r') as csvfile:
		data = csv.reader(csvfile, delimiter=',')
			
		print('Reading %s_topological_network.csv...' % (prog_languages[prog_lang_id]))
		t_network = []

		for row in data:
			dev_id_1 = int(row[0])
			dev_id_2 = int(row[1])

			t_network.append((dev_id_1, dev_id_2))
	csvfile.close()	

	with open('../Files/topological_metrics.csv', 'a') as a:
		metrics_file = csv.writer(a, delimiter=',')

		print('Writing topological metrics for', prog_languages[prog_lang_id])

		for dev_pair in t_network:
			neighborhood_overlap = nx.jaccard_coefficient(G, [dev_pair])
			adamic_acar = nx.adamic_adar_index(G, [dev_pair])
			preferential_attachment = nx.preferential_attachment(G, [dev_pair])

			for u,v,p in neighborhood_overlap:
				NO = p
			for u,v,p in adamic_acar:
				AA = p
			for u,v,p in preferential_attachment:
				PA = p
				
			metrics_file.writerow([prog_lang_id, dev_pair[0], dev_pair[1], NO, AA, PA])
	a.close()