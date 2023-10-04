class ParseData(object):
    def depth(self, node, graph):
        if node not in graph or len(graph[node]) == 0:
            return 1
        child_depth = [self.depth(child, graph) for child in graph[node]]
        return 1 + max(child_depth)

    def get_input_data(self, file_name=""):
        input_data = self.create_input_graph(file_name)
        input_graph = input_data['graph']
        leaf_nodes = input_data['leaf_nodes']

        tree_depth = self.depth(list(input_graph.keys())[0], input_graph)
        return {"input_graph": input_graph, "tree_depth": tree_depth, 'leaf_nodes': leaf_nodes}

    def create_input_graph(self, file_name=""):
        nodes = {}
        graph = {}
        return_data = {'graph': graph, 'leaf_nodes': nodes}
        if not file_name:
            return return_data
        input_file = open(f"minimax/parse_data/{file_name}", "r")

        count = 0
        for line in input_file:
            count += 1
            line_text = line.strip()
            if "#" in line_text:
                continue
            print("Line{}: {}".format(count, line.strip()))

            if "=" in line_text:
                components = line_text.split("=")
                nodes[components[0].strip()] = int(components[1].strip())

            if ":" in line_text:
                node_neighbors = line_text.split(":")
                node = node_neighbors[0].strip()
                neighbors = node_neighbors[1].split("[")[1].split("]")[0].split(",")

                for ch in neighbors:
                    if ch == "[" or ch == "]" or ch == "," or ch == " ":
                        continue
                    ch = ch.strip()
                    # print('node: ', ch)
                    if node not in graph:
                        graph[node] = []
                    graph[node].append(ch)

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

        return_data = {'graph': graph, 'leaf_nodes': nodes}
        return return_data


if __name__ == "__main__":
    p = ParseData()
    p.create_input_graph()
