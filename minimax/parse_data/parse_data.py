class ParseData(object):
    def __init__(self):
        self.input_file = open("input1", 'r')

    def create_input_graph(self):
        nodes = {}
        graph = {}
        count = 0
        for line in self.input_file:
            count += 1
            line_text = line.strip()
            if "#" in line_text:
                continue
            print("Line{}: {}".format(count, line.strip()))

            if "=" in line_text:
                components = line_text.split("=")
                nodes[components[0].strip()] = components[1].strip()

            if ":" in line_text:
                node_neighbors = line_text.split(':')
                node = node_neighbors[0].strip()
                neighbors = node_neighbors[1].split('[')[1].split(']')[0].split(',')

                for ch in neighbors:
                    if ch == '[' or ch == ']' or ch == ',' or ch == ' ':
                        continue
                    ch = ch.strip()
                    # print('node: ', ch)
                    if node not in graph:
                        graph[node] = []
                    graph[node].append(ch)
        print('nodes: ', nodes)

        count_nodes = 0
        for parent, children in graph.items():
            # print('children: ', children)
            children_values = []
            count_nodes += 1
            for child in children:
                count_nodes += 1
                # print('child: ', child)
                node_value = nodes.get(child, None)
                # print('node_value: ', node_value)
                if node_value:
                    children_values.append(int(node_value))
            # print('children_values: ', children_values)
            if children_values:
                graph[parent] = children_values

        print('final_input: ', graph)
        return graph, count_nodes


if __name__ == '__main__':
    p = ParseData()
    p.create_input_graph()
