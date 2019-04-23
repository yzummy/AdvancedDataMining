# from geopy.distance import geodesic
# print(geodesic((39.907655, 116.404194),(39.908806, 116.417778)).kilometers)


# from collections import defaultdict
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#     d[k].append(v)
# sorted(d.items())

import pickle
def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
graph = load_obj("graph_750m")
print(graph)