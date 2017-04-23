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
        print('Reading tieness unsorted to %s metric for %s...' % (metric_name, language_acronym)) 
        
        with open("../Files/T_%s_%s_unsorted.csv" % (language_acronym, metric_name), "r") as arq:
            metric = csv.reader(arq, delimiter=',')

            next(metric)

            for row in metric:
                dev_id_1 = int(row[1])
                dev_id_2 = int(row[2])
                tieness = row[3]

                programming_language_id = 1 if language_acronym == 'JS' else 2

                if (programming_language_id, dev_id_1, dev_id_2) in metric_dict:
                    print("ERRO! Tupla existente no dict")
                else:
                    metric_dict[programming_language_id, dev_id_1, dev_id_2] = tieness

        arq.close()

    # ordena dict da métrica
    print("Sorting %s metric dict..." % (metric_name))
    metric_sort = collections.OrderedDict(sorted(metric_dict.items()))

    print('Writing tieness metric to %s...' % (metric_name))
    with open('../Files/T_%s.csv' % (metric_name), 'w') as w:
        metric_file = csv.writer(w, delimiter=',')

        # escreve cabeçalho
        metric_file.writerow(["programming_language_id", "developer_id_1", "developer_id_2", "tieness"])

        # a soma do tempo de contribuição é dividida pelo tempo total da rede
        for row in metric_sort:
            metric_file.writerow([row[0], row[1], row[2], metric_sort[row]])
    w.close()




