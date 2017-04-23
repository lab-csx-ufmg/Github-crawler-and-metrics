# script para geração da tabela contendo todas as métricas da rede

# cabeçalho da arquivo gerado (social_network_metrics.csv):
# 0 - programming_language
# 1 - developer_id_1
# 2 - developer_id_2
# 3 - NO
# 4 - AA
# 5 - PA
# 6 - SR
# 7 - T_SR
# 8 - RA_SR
# 9 - JCSR
# 10 - T_JCSR
# 11 - RA_JCSR
# 12 - JCOSR
# 13 - T_JCOSR
# 14 - RA_JCOSR
# 15 - JWCOSR
# 16 - T_JWCOSR
# 17 - RA_JWCOSR
# 18 - PC
# 19 - T_PC
# 20 - RA_PC
# 21 - GPC
# 22 - T_GPC
# 23 - RA_GPC

import sys, csv, operator, collections

# cria dict para todas as métricas calculadas
network_all_metrics = {}

# lê cada métrica para adicioná-la à tabela final

# leitura do arquivo com métricas topológicas
print("Reading topological_metrics.csv...")
with open('../Files/topological_metrics.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,n_overlap,a_adar,p_att
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			print("WARNING - duplicated tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
		else:
			# inclui métricas no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2] = [row[3], row[4], row[5], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
r.close()
print("Finished read topological_metrics.csv")

# leitura do arquivo com métrica SR
print("Reading SR.csv...")
with open('../Files/SR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,SR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][3] = row[3]
		else:
			print("WARNING - non-existent SR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read SR.csv")

# leitura do arquivo com métrica T_SR
print("Reading T_SR.csv...")
with open('../Files/T_SR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,T_SR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][4] = row[3]
		else:
			print("WARNING - non-existent T_SR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read T_SR.csv")

# leitura do arquivo com métrica SR
print("Reading RA_SR.csv...")
with open('../Files/RA_SR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,RA_SR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][5] = row[3]
		else:
			print("WARNING - non-existent RA_SR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read RA_SR.csv")

# leitura do arquivo com métrica JCSR
print("Reading JCSR.csv...")
with open('../Files/JCSR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,JCSR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][6] = row[3]
		else:
			print("WARNING - non-existent JCSR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read JCSR.csv")

# leitura do arquivo com métrica T_JCSR
print("Reading T_JCSR.csv...")
with open('../Files/T_JCSR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,T_JCSR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][7] = row[3]
		else:
			print("WARNING - non-existent T_JCSR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read T_JCSR.csv")

# leitura do arquivo com métrica RA_JCSR
print("Reading RA_JCSR.csv...")
with open('../Files/RA_JCSR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,RA_JCSR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][8] = row[3]
		else:
			print("WARNING - non-existent RA_JCSR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read RA_JCSR.csv")

# leitura do arquivo com métrica JCOSR
print("Reading JCOSR.csv...")
with open('../Files/JCOSR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,JCOSR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][9] = row[3]
		else:
			print("WARNING - non-existent JCOSR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read JCOSR.csv")

# leitura do arquivo com métrica T_JCOSR
print("Reading T_JCOSR.csv...")
with open('../Files/T_JCOSR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,T_JCOSR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][10] = row[3]
		else:
			print("WARNING - non-existent T_JCOSR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read T_JCOSR.csv")

# leitura do arquivo com métrica RA_JCOSR
print("Reading RA_JCOSR.csv...")
with open('../Files/RA_JCOSR.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,RA_JCOSR
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][11] = row[3]
		else:
			print("WARNING - non-existent RA_JCOSR tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read RA_JCOSR.csv")

# leitura do arquivo com métrica JWCOSR
print("Reading NL.csv (metric JWCOSR)...")
with open('../Files/NL.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,NL
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][12] = row[3]
		else:
			print("WARNING - non-existent NL (metric JWCOSR) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read NL.csv (metric JWCOSR)")

# leitura do arquivo com métrica T_JWCOSR
print("Reading T_NL.csv (metric T_JWCOSR)...")
with open('../Files/T_NL.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,T_NL
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][13] = row[3]
		else:
			print("WARNING - non-existent T_NL (metric T_JWCOSR) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read T_NL.csv (metric T_JWCOSR)")

# leitura do arquivo com métrica RA_JWCOSR
print("Reading RA_NL.csv (metric RA_JWCOSR)...")
with open('../Files/RA_NL.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,RA_NL
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][14] = row[3]
		else:
			print("WARNING - non-existent RA_NL (metric RA_JWCOSR) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read RA_NL.csv (metric RA_JWCOSR)")

# leitura do arquivo com métrica PC
print("Reading PSC.csv (metric PC)...")
with open('../Files/PSC.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,PSC
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][15] = row[3]
		else:
			print("WARNING - non-existent PSC (metric PC) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read PSC.csv (metric PC)")

# leitura do arquivo com métrica T_PC
print("Reading T_PSC.csv (metric T_PC)...")
with open('../Files/T_PSC.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,T_PSC
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][16] = row[3]
		else:
			print("WARNING - non-existent T_PSC (metric T_PC) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read T_PSC.csv (metric T_PC)")

# leitura do arquivo com métrica RA_PC
print("Reading RA_PSC.csv (metric RA_PC)...")
with open('../Files/RA_PSC.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,RA_PSC
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][17] = row[3]
		else:
			print("WARNING - non-existent RA_PSC (metric RA_PC) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read RA_PSC.csv (metric RA_PC)")

# leitura do arquivo com métrica GPC
print("Reading CT.csv (metric GPC)...")
with open('../Files/CT.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,CT
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][18] = row[3]
		else:
			print("WARNING - non-existent CT (metric GPC) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read CT.csv (metric GPC)")

# leitura do arquivo com métrica T_GPC
print("Reading T_CT.csv (metric T_GPC)...")
with open('../Files/T_CT.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,T_CT
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][19] = row[3]
		else:
			print("WARNING - non-existent T_CT (metric T_GPC) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read T_CT.csv (metric T_GPC)")

# leitura do arquivo com métrica RA_GPC
print("Reading RA_CT.csv (metric RA_GPC)...")
with open('../Files/RA_CT.csv', 'r') as r:
	metric_file = csv.reader(r, delimiter=',')

	next(metric_file) # cabeçalho
	# programming_language_id,developer_id_1,developer_id_2,RA_CT
	
	for row in metric_file:
		programming_language_id = int(row[0])
		dev_id_1 = int(row[1])
		dev_id_2 = int(row[2])
		
		if (programming_language_id, dev_id_1, dev_id_2) in network_all_metrics:
			# inclui métrica no dict
			network_all_metrics[programming_language_id, dev_id_1, dev_id_2][20] = row[3]
		else:
			print("WARNING - non-existent RA_CT (metric RA_GPC) tuple in topological metrics! -", programming_language_id, dev_id_1, dev_id_2)
r.close()
print("Finished read RA_CT.csv (metric RA_GPC)")

# ordena o dict completo para escrita no arquivo final
network_all_metrics_sorted = collections.OrderedDict(sorted(network_all_metrics.items()))

# escreve tabela final com todas as métricas para o data set
print("Writing social_network_metrics.csv...")
with open('../DataSet/social_network_metrics.csv', 'w') as w:
 	network_file = csv.writer(w, delimiter=',')
 	
 	# cabeçalho
 	network_file.writerow(['programming_language_id', 'developer_id_1', 'developer_id_2', 'NO', 'AA', 'PA', 'SR', 'T_SR', 'RA_SR', 'JCSR', 'T_JCSR', 'RA_JCSR', 'JCOSR', 'T_JCOSR', 'RA_JCOSR', 'JWCOSR', 'T_JWCOSR', 'RA_JWCOSR', 'PC', 'T_PC', 'RA_PC', 'GPC', 'T_GPC', 'RA_GPC']) 
 	
 	for row in network_all_metrics_sorted: 
 		network_file.writerow([row[0], row[1], row[2], network_all_metrics_sorted[row][0], network_all_metrics_sorted[row][1], network_all_metrics_sorted[row][2], network_all_metrics_sorted[row][3], network_all_metrics_sorted[row][4], network_all_metrics_sorted[row][5], network_all_metrics_sorted[row][6], network_all_metrics_sorted[row][7], network_all_metrics_sorted[row][8], network_all_metrics_sorted[row][9], network_all_metrics_sorted[row][10], network_all_metrics_sorted[row][11], network_all_metrics_sorted[row][12], network_all_metrics_sorted[row][13], network_all_metrics_sorted[row][14], network_all_metrics_sorted[row][15], network_all_metrics_sorted[row][16], network_all_metrics_sorted[row][17], network_all_metrics_sorted[row][18], network_all_metrics_sorted[row][19], network_all_metrics_sorted[row][20]])
w.close()