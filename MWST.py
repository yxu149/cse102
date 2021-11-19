#!/usr/local/bin/python3

import sys
import __main__


class Graph():

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w, index):
        self.graph.append([u, v, w, index])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root

        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def Kruskal_MST(self, file_out):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while i < self.vertices - 1:
            u, v, w, index = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w, index])
                self.union(parent, rank, x, y)

        min_cost = 0

        for u, v, weight, index in result:
            weight = weight + 0.0
            min_cost += weight + 0.0
            line_str = str(index).rjust(4, ' ') + ': (' + str(u) + ', ' + str(v) + ') ' + str(weight)
            file_out.write(line_str)
        file_out.write('Total Weight =', "{0:.2f}".format(min_cost))


def main():
    if len(sys.argv) != 3:
        print('Usage error! Please enter exactly 2 arguments!\n')
        sys.exit(2)

    name_in = sys.argv[1]
    name_out = sys.argv[2]

    file_in = open(name_in, 'r')
    file_out = open(name_out, 'x')

    lines = []
    for line in file_in:
        lines.append(line)

    num_line = int(lines[1])

    graph = Graph(num_line)
    args = []

    del lines[0:2]

    line_num = 1
    for line in lines:
        for i in range(0, 3):
            args.append(line.split(' ')[i])

        args[2] = args[2].removesuffix('\n')
        graph.add_edge(int(args[0]), int(args[1]), int(args[2]), line_num)
        args.clear()
        line_num += 1

    graph.Kruskal_MST(file_out)
    file_out.close()
    file_in.close()
    return


if __name__ == '__main__':
    sys.exit(main())
