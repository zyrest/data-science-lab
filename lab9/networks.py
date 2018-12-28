from collections import defaultdict
from lab9 import db_en, db_jp

import networkx as nx

eq_time = 1299822360


def create_net(data):
    G = nx.Graph()
    # w_nodes = defaultdict(defaultdict)
    for record in data:
        c_nick = record['nick']
        if c_nick not in G:
            G.add_node(c_nick)

        content = str(record['content'])
        if content:
            while '@' in content:
                ind = content.index('@')
                n_nick = ''
                while content[ind] != ' ' and content[ind] != ':' and ind < len(content)-1:
                    ind = ind + 1
                    if content[ind] != ':':
                        n_nick += content[ind]
                if n_nick not in G:
                    G.add_node(n_nick)

                G.add_edge(c_nick, n_nick)

                # if n_nick in nx.neighbors(G, c_nick):
                #     if c_nick in w_nodes:
                #         if n_nick in w_nodes[c_nick]:
                #             w_nodes[c_nick][n_nick] += 1
                # else:
                #     w_nodes[c_nick][n_nick] = 1

                content = content[ind+1:]
    return G


def drop_diff_point(G1, G2):
    for node in list(G1):
        if node not in G2:
            G1.remove_node(node)

    for node in list(G2):
        if node not in G1:
            G2.remove_node(node)


def init_net(db):
    data = db.find()

    data_bef = []
    data_aft = []
    for row in data:
        if row['date'] >= eq_time:
            data_aft.append(row)
        else:
            data_bef.append(row)

    G_before = create_net(data_bef)
    G_after = create_net(data_aft)
    drop_diff_point(G_before, G_after)

    db_name = db.name
    nx.write_gml(G_before, db_name+'-before.gml')
    nx.write_gml(G_after, db_name+'-after.gml')


if __name__ == '__main__':
    init_net(db_en)
    init_net(db_jp)
