"""
This program draws the networks of artists and users
"""

import networkx as nx
from matplotlib import pyplot as plt
import csv

"""
Parameters
ratio: to determine if a user's play count of a certain artist is beyond a certain threshold
freq: to determine if the number of shared users of two artists is beyond a certain threshold
"""
def graph_data(ratio, freq):
    with open('artists_users_playcount_ratio.csv', encoding='utf-8') as inf:
        incsv = csv.reader(inf)
        next(incsv)

        artist = {}
        temp = next(incsv)[0]
        for line in incsv:
            if float(line[3]) > ratio and line[0] != temp:
                if (line[0], temp) in artist or (temp, line[0]) in artist:
                    try:
                        artist[(line[0], temp)] += 1
                    except:
                        artist[(temp, line[0])] += 1
                else:
                    artist[(line[0], temp)] = 1
                temp = line[0]

    for key in list(artist.keys()):
        if int(artist[key]) < freq:
            del artist[key]

    return artist

def main():
    params = [10, 50, 100, 200, 300, 400, 500]
    result = {}
    for param in params:
        result[param] = graph_data(0.1, param)

    for key, value in result.items():
        G = nx.Graph()
        for data in value:
            G.add_node(data[0])
            G.add_node(data[1])
            G.add_edge(data[0], data[1])
        nx.write_gml(G, 'graph/artist_user_' + str(key) + '.gml')

if __name__ == '__main__':
    main()
