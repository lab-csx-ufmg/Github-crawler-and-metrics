#!/usr/bin/env python2.7

import networkx as nx
import csv

class GraphGenerator:
  def __init__(self, file_name):
    self.create_graph(file_name)

  def create_graph(self, file_name):
    print ("Creating graph...")
    self.graph = nx.Graph()

    with open(file_name) as csvfile:
      reader = csv.DictReader(csvfile, delimiter=',')
      next(reader)
      for row in reader:
        # Add edge
        self.graph.add_edge(int(row["n1"]), int(row["n2"]), weight=float(row["weight"]))

  def weight_distr(self):
    weights = {}
    for edge in self.graph.edges():
      weight = self.graph[edge[0]][edge[1]]['weight']
      if weight in weights:
        weights[weight] += 1
      else:
        weights[weight] = 1

    return weights

  def order_nodes(self, u, v):
    array = sorted([u, v])
    return (array[0], array[1])

  def propagation_coefficient(self, programming_language, metric_name):
    print ("Calculating weighted degrees...")
    w_degree = self.graph.degree(weight='weight')

    print ("Calculating propagation coefficient: RA_%s_%s.csv..." % (programming_language, metric_name))
    m = {}
    out = open('../Files/RA_%s_%s.csv' % (programming_language, metric_name), "w")

    for x in self.graph.nodes():
      x_nbrs = self.graph.neighbors(x)

      for y in x_nbrs:
        xy = self.order_nodes(x, y)
        if not xy in m:
          w_xy = float(self.graph[x][y]['weight'])

          # evitar erro de divisão por zero
          if w_degree[x] != 0:
            m[xy] = w_xy/w_degree[x]
          else:
            m[xy] = 0

          y_nbrs = self.graph.neighbors(y)

          if x in y_nbrs:
            y_nbrs.remove(x)

          for z in y_nbrs:
            if z in x_nbrs:
              w_xz = float(self.graph[x][z]['weight'])
              w_zy = float(self.graph[z][y]['weight'])

              # evitar erro de divisão por zero
              if w_degree[x] != 0 and w_degree[z] != 0:
                m[xy] += (w_xz * w_zy)/(w_degree[x] * w_degree[z])

          out.write("(%d, %d) %f\n" % (x, y, m[xy]))

    out.close()
            
# cria lista de métricas que terão a RESOURCE ALLOCATION (RA) calculada
metric_list = ['SR', 'JCSR', 'JCOSR', 'NL', 'PSC', 'CT']

# reescreve arquivos retirando cabeçalho e dividindo linguagens
for metric_name in metric_list:
  print('Reading %s.csv and writing JS_%s_to_calc_RA.csv and RB_%s_to_calc_RA.csv...' % (metric_name, metric_name, metric_name))
  with open('../Files/%s.csv' % (metric_name), 'r') as r:
    data_r = csv.reader(r, delimiter=',')
    next(data_r) # cabeçalho

    with open('../Files/JS_%s_to_calc_RA.csv' % (metric_name), 'w') as w1:
      data_WJS = csv.writer(w1, delimiter=',')

      with open('../Files/RB_%s_to_calc_RA.csv' % (metric_name), 'w') as w2:
        data_WRB = csv.writer(w2, delimiter=',')

        # cabeçalhos
        data_WJS.writerow(['n1', 'n2', 'weight'])
        data_WRB.writerow(['n1', 'n2', 'weight'])

        for row in data_r:
          prog_lang_read = int(row[0])

          if prog_lang_read == 1:
            data_WJS.writerow([row[1], row[2], row[3]])
          elif prog_lang_read == 2:
            data_WRB.writerow([row[1], row[2], row[3]])
      w2.close()
    w1.close()
  r.close()

  print('Generating graph to %s metric for JS...' % (metric_name))

  gg = GraphGenerator('../Files/JS_%s_to_calc_RA.csv' % (metric_name))
  gg.propagation_coefficient('JS', metric_name)

  print('Generating graph to %s metric for RB...' % (metric_name))

  gg = GraphGenerator('../Files/RB_%s_to_calc_RA.csv' % (metric_name))
  gg.propagation_coefficient('RB', metric_name)