import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def average_deg(G, name):
    d = nx.degree(G)
    print('{} 平均度: {}'.format(name, np.array(list([i[1] for i in d])).mean()))


def largest_com(G, name):
    largest_c = max(nx.connected_components(G), key=len)
    print('{} 的最大联通成分的大小为: {}'.format(name, len(largest_c)))


def average_clu(G, name):
    c = nx.average_clustering(G)
    print('{} 的平均群聚系数为: {}'.format(name, c))


# 个人层面度分析
def individual_degree(G1, G2, name):
    nodes1 = G1.nodes
    nodes2 = G2.nodes
    degree1 = []
    degree2 = []
    for node in nodes1:
        if node in nodes2:
            degree1.append(G1.degree(node))
            degree2.append(G2.degree(node))

    plt.title(name)
    plt.xlabel('before')
    plt.ylabel('after')
    plt.loglog(degree1, degree2, 'o')
    plt.show()


# 累计度分析
def cumlutive_degree(G):
    degree = []
    list = G.degree()
    for node in list:
        degree.append(node[1])
    xs = degree

    dist_keys = range(min(xs), max(xs)+1)
    pdf = dict([(k, 0) for k in dist_keys])
    for x in xs:
        pdf[x] += 1
    pdf_temp = pdf
    scope = range(min(pdf), max(pdf)+1)
    for degree in scope:
        k = degree + 1
        while k <= max(pdf):
            pdf[degree] += pdf_temp[k]
            k += 1
    return pdf


def draw_degree_chart(G1, G2, name):
    degree1 = cumlutive_degree(G1)
    y1 = np.array(list(degree1.values()))
    y1 = y1 / y1[0]
    x1 = range(len(degree1))
    color = 'r^'
    line = plt.loglog(x1, y1, color)
    plt.legend(line, 'before')

    degree2 = cumlutive_degree(G2)
    y2 = np.array(list(degree2.values()))
    y2 = y2 / y2[0]
    x2 = range(len(degree2))
    color = 'g^'
    line = plt.loglog(x2, y2, color)
    plt.legend(line, 'after')

    plt.title(name)
    plt.show()


if __name__ == '__main__':
    G_en_bef = nx.read_gml('./data/lab9_en-before.gml')
    G_en_aft = nx.read_gml('./data/lab9_en-after.gml')

    G_jp_bef = nx.read_gml('./data/lab9_jp-before.gml')
    G_jp_aft = nx.read_gml('./data/lab9_jp-after.gml')

    average_deg(G_en_bef, 'EN average degree before earthquake')
    average_deg(G_en_aft, 'EN average degree after earthquake')
    average_deg(G_jp_bef, 'JP average degree before earthquake')
    average_deg(G_jp_aft, 'JP average degree after earthquake')

    largest_com(G_en_bef, 'EN largest components before earthquake')
    largest_com(G_en_aft, 'EN largest components after earthquake')
    largest_com(G_jp_bef, 'JP largest components before earthquake')
    largest_com(G_jp_aft, 'JP largest components after earthquake')

    average_clu(G_en_bef, 'EN average cluster before earthquake')
    average_clu(G_en_aft, 'EN average cluster after earthquake')
    average_clu(G_jp_bef, 'JP average cluster before earthquake')
    average_clu(G_jp_aft, 'JP average cluster after earthquake')

    individual_degree(G_en_bef, G_en_aft, "EN individual degree")
    individual_degree(G_jp_bef, G_jp_aft, "JP individual degree")

    draw_degree_chart(G_en_bef, G_en_aft, "EN cumlutive degree")
    draw_degree_chart(G_jp_bef, G_jp_aft, "JP cumlutive degree")
