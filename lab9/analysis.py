import networkx as nx
import numpy as np


def average_deg(G, name):
    d = nx.degree(G)
    print('{} 平均度:'.format(name))
    print(np.ndarray(list(d.values())).mean())


def largest_com(G, name):
    largest_c = max(nx.connected_components(G), key=len)
    print('{} 的最大联通成分的大小为: {}'.format(name, len(largest_c)))


def average_clu(G, name):
    c = nx.average_clustering(G)
    print('{} 的平均群聚系数为: {}'.format(name, c))


if __name__ == '__main__':
    G_en_bef = nx.read_gml('./data/lab9_en-before.gml')
    G_en_aft = nx.read_gml('./data/lab9_en-after.gml')

    G_jp_bef = nx.read_gml('./data/lab9_jp-before.gml')
    G_jp_aft = nx.read_gml('./data/lab9_jp-after.gml')

    average_deg(G_en_bef, 'en_before')
