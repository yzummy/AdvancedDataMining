import numpy as np
import sys
import pickle as pkl
import networkx as nx
import scipy.sparse as sp


def parse_index_file(filename):
    index = []
    for line in open(filename):
        index.append(int(line.strip()))
    return index


def load_data(dataset):
    # load the data: x, tx, allx, graph
    names = ['community.allx', 'graph_500m']
    objects = []
    for i in range(len(names)):
        with open("gae/data/{}.pkl".format(names[i]), 'rb') as f:
            if sys.version_info > (3, 0):
                objects.append(pkl.load(f, encoding='latin1'))
            else:
                objects.append(pkl.load(f))
    allx, graph = tuple(objects)

    features = allx.tolil()
    adj = nx.adjacency_matrix(nx.from_dict_of_lists(graph))

    return adj, features
