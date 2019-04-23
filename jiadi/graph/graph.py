import pickle
from geopy.distance import geodesic
from collections import defaultdict
# from numba import jit


def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


# @jit

sell = load_obj("sell_data")
print(list(sell))
coordinates = []
with open("newhouse_basic_formated.txt", 'r', encoding='utf-8') as f:
    line = f.readline()[1:]
    # print(line[:-1], len(line))
    # cnt = 1
    while line:
        if line[0:3] == 'bid':
            index_ori = int(line.split()[1])
            line = f.readline()
            lat = float(line.split()[1])
            line = f.readline()
            lng = float(line.split()[1])
            # print(lat,lng)
            if index_ori in list(sell):
                index_new = list(sell).index(index_ori)
                # print(index_ori, index_new)
                coordinates.insert(index_new, {'index_ori': index_ori, 'lat': lat, 'lng': lng})
        line = f.readline()
        
graph = defaultdict(list)
for i in range(coordinates.__len__()):
    graph[i].append(i)
for i in range(coordinates.__len__() - 1):
    print(i)
    for j in range(i + 1, coordinates.__len__()):
        location1 = (coordinates[i]['lat'], coordinates[i]['lng'])
        location2 = (coordinates[j]['lat'], coordinates[j]['lng'])
        dis = geodesic(location1, location2).kilometers
        if dis <= 8:
            graph[i].append(j)
            graph[j].append(i)
save_obj(graph, "graph_8km")
