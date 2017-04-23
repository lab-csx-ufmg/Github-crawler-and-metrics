#*************************************************************************************#
#* Codigo para calcular tieness.                                                     *#
#* Data: 20 de setembro de 2016                                                      *#
#* Autora: Michele A. Brandao                                                        *#
#* http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html    *# 
#*************************************************************************************#

import csv, collections

# cria lista de métricas que terão a tieness (T_) calculada
metric_list = ['SR', 'JCSR', 'JCOSR', 'NL', 'PSC', 'CT'] 

# reescreve arquivos retirando cabeçalho e dividindo linguagens
for metric_name in metric_list:  
    metric_dict = {}

    for language_acronym in ['JS', 'RB']:
        print('Reading resource allocation unsorted to %s metric for %s...' % (metric_name, language_acronym)) 
        
        with open("../Files/RA_%s_%s_unsorted.csv" % (language_acronym, metric_name), "r") as arq:
            metric = csv.reader(arq, delimiter=' ')

            for row in metric:
                dev_id_1 = int(row[0][1:-1])
                dev_id_2 = int(row[1][0:-1])
                tieness = row[2]

                programming_language_id = 1 if language_acronym == 'JS' else 2

                if dev_id_1 < dev_id_2:
                    if (programming_language_id, dev_id_1, dev_id_2) in metric_dict:
                        print("ERRO! Tupla existente no dict")
                    else:
                        metric_dict[programming_language_id, dev_id_1, dev_id_2] = tieness
                else:
                    if (programming_language_id, dev_id_2, dev_id_1) in metric_dict:
                        print("ERRO! Tupla existente no dict")
                    else:
                        metric_dict[programming_language_id, dev_id_2, dev_id_1] = tieness

        arq.close()

    # ordena dict da métrica
    print("Sorting %s metric dict..." % (metric_name))
    metric_sort = collections.OrderedDict(sorted(metric_dict.items()))

    print('Writing resource allocation metric to %s...' % (metric_name))
    with open('../Files/RA_%s.csv' % (metric_name), 'w') as w:
        metric_file = csv.writer(w, delimiter=',')

        # escreve cabeçalho
        metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "RA"])

        # a soma do tempo de contribuição é dividida pelo tempo total da rede
        for row in metric_sort:
            metric_file.writerow([row[0], row[1], row[2], metric_sort[row]])
    w.close()




