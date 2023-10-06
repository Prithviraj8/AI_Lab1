import os

from .exceptions import ExceptionHandling, Messages


class ParseData(object):
    def depth(self, node, graph):
        if node not in graph or len(graph[node]) == 0:
            return 1
        child_depth = [self.depth(child, graph) for child in graph[node]]
        return 1 + max(child_depth)

    def get_root(self, input_graph):
        exception_handling = ExceptionHandling()
        root_data_obj = exception_handling.root_failure(input_graph)
        return root_data_obj

    def check_node_failure(self, input_graph, leaf_nodes):
        exception_handling = ExceptionHandling()
        node_data_obj = exception_handling.node_failure(input_graph, leaf_nodes)
        return node_data_obj

    def check_leaf_failure(self, input_graph, leaf_nodes):
        exception_handling = ExceptionHandling()
        leaf_data_obj = exception_handling.leaf_failure(input_graph, leaf_nodes)
        return leaf_data_obj

    def get_input_data(self, file_name=""):
        result = {
            "input_graph": None,
            "tree_depth": None,
            "leaf_nodes": None,
            "message": None
        }
        input_data = self.create_input_graph(file_name)
        if input_data['message'] is not None:
            result['message'] = input_data['message']
            return result
        input_graph = input_data["graph"]
        leaf_nodes = input_data["leaf_nodes"]

        tree_depth = self.depth(list(input_graph.keys())[0], input_graph)
        return {
            "input_graph": input_graph,
            "tree_depth": tree_depth,
            "leaf_nodes": leaf_nodes,
            "message": None
        }

    def create_input_graph(self, file_name=""):
        leaf_nodes = {}
        graph = {}
        return_data = {"graph": graph, "leaf_nodes": leaf_nodes, 'message': None}
        if not file_name:
            return_data['message'] = 'No filename provided'
            return return_data
        try:
            input_file = open(f"minimax/parse_data/{file_name}", "r")
        except Exception as e:
            return_data['message'] = Messages.FILE_INPUT
            return return_data
        # print("\n--Reading Input text file --")
        count = 0
        for line in input_file:
            count += 1
            line_text = line.strip()
            if line_text.startswith("#"):
                continue
            # print("Line{}: {}".format(count, line.strip()))

            if "=" in line_text:
                components = line_text.split("=")
                leaf_nodes[components[0].strip()] = int(components[1].strip())

            if ":" in line_text:
                node_neighbors = line_text.split(":")
                node = node_neighbors[0].strip()
                neighbors = node_neighbors[1].split("[")[1].split("]")[0].split(",")

                for ch in neighbors:
                    if ch == "[" or ch == "]" or ch == "," or ch == " ":
                        continue
                    ch = ch.strip()
                    if node not in graph:
                        graph[node] = []
                    graph[node].append(ch)
        print("\n")
        return_data["graph"] = graph
        return_data["leaf_nodes"] = leaf_nodes
        return return_data


if __name__ == "__main__":
    p = ParseData()
    p.create_input_graph("input_file.txt")
