#*************************************************************************************#
#* Codigo para calcular tieness.                                                     *#
#* Data: 20 de setembro de 2016                                                      *#
#* Autora: Michele A. Brandao                                                        *#
#* http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html    *# 
#*************************************************************************************#

import csv

############################# Usando dicionarios #############################   
def tieness(programming_language, metric_name):
    d_coauthor=dict() 
    d_weight=dict()

    with open("../Files/%s_%s_to_calc_RA.csv" % (programming_language, metric_name), "r") as arq:
        print("Reading file %s_%s_to_calc_RA.csv..." % (programming_language, metric_name))
        
        pairs = csv.reader(arq, delimiter=',');
        
        next(pairs)

        for pair in pairs:
            if pair[0] in d_coauthor:
                d_coauthor[pair[0]].append(pair[1])
                d_weight[pair[0]].append(pair[2])
            else:
                d_coauthor[pair[0]] = [pair[1]]
                d_weight[pair[0]] = [pair[2]]
                
            if pair[1] in d_coauthor:
                d_coauthor[pair[1]].append(pair[0])
                d_weight[pair[1]].append(pair[2])
            else:
                d_coauthor[pair[1]] = [pair[0]]
                d_weight[pair[1]] = [pair[2]]
    arq.close()

    #Arquivo para armazenar valor da nova metrica
    print("Creating file T_%s_%s.csv..." % (programming_language, metric_name))
    sn = open('../Files/T_%s_%s_part1.csv' % (programming_language, metric_name), 'w+')
    aux1 = csv.writer(sn, delimiter=',')
    aux1.writerows([['source','target','weight','intersection','union','neighborhoodOverlap','changeNO']])

    with open("../Files/%s_%s_to_calc_RA.csv" % (programming_language, metric_name), "r") as arq:
        print("Reading file %s_%s_to_calc_RA.csv and writing metric..." % (programming_language, metric_name))
        pairs = csv.reader(arq, delimiter=',');
        
        next(pairs) # cabeçalho

        for pair in pairs:
            if int(pair[0]) < int(pair[1]):
                intersection = set(d_coauthor[pair[0]]).intersection(d_coauthor[pair[1]])
                size_intersection = len(intersection)

                size_intersection_changed = len(intersection) + 1  #Adicionamos 1 para representar o link que existe entre o par de pesquisadores

                union = set(d_coauthor[pair[0]]).union(d_coauthor[pair[1]])
                size_union = len(union)-2

                if size_union!=0:
                    changeNO = size_intersection_changed/(1+float(size_union))
                    aux1.writerows([[pair[0],pair[1],d_weight[pair[0]][d_coauthor[pair[0]].index(pair[1])],size_intersection,size_union,(size_intersection/float(size_union)),changeNO]])

                if size_union==0:
                    aux1.writerows([[pair[0],pair[1],d_weight[pair[0]][d_coauthor[pair[0]].index(pair[1])],size_intersection,size_union,0,0]])
    arq.close()
        
##############################################################################       
        
if __name__=='__main__': 

    # cria lista de métricas que terão a tieness (T_) calculada
    metric_list = ['SR', 'JCSR', 'JCOSR', 'NL', 'PSC', 'CT'] 

    # reescreve arquivos retirando cabeçalho e dividindo linguagens
    for metric_name in metric_list:  
        print('Calculating tieness to %s metric for JS...' % (metric_name)) 
        tieness('JS', metric_name)

        print('Calculating tieness to %s metric for RB...' % (metric_name)) 
        tieness('RB', metric_name)
        


