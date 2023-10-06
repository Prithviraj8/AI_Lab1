import argparse
import logging
import sys

from parse_data.parse_data import ParseData


class Minimax:
    def __init__(self):
        self.root = None
        self.max = False
        self.ab = False
        self.verbose = False
        self.range = []
        self.filename = None
        self.input_graph = {}
        self.tree_depth = 0
        self.leaf_nodes = {}

    def add_arguements(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d",
            "--debug",
            help="Print lots of debugging statements",
            action="store_const",
            dest="loglevel",
            const=logging.DEBUG,
            default=logging.WARNING,
        )
        parser.add_argument(
            "-v",
            "--verbose",
            help="Be verbose",
            action="store_const",
            dest="loglevel",
            const=logging.INFO,
        )
        parser.add_argument(
            "-ab", help="Enable Alpha Beta Pruning", action="store_true"
        )
        parser.add_argument("-range", help="Range of values for nodes", type=int)
        parser.add_argument("max", help="Max for the root node")
        parser.add_argument(
            "filename",
            help="Name of the input text file in the current directory"
        )
        args = parser.parse_args()
        logging.basicConfig(level=args.loglevel)
        return args

    def assign_input_data(self):
        parse_data = ParseData()
        input_data = parse_data.get_input_data(self.filename)
        if input_data['message'] is not None:
            return input_data

        self.input_graph = input_data["input_graph"]
        self.tree_depth = input_data["tree_depth"]
        self.leaf_nodes = input_data["leaf_nodes"]
        return {}

    def read_arguements(self):
        args = self.add_arguements()
        if '-v' in sys.argv:
            self.verbose = True
        if args.range:
            self.range = [-args.range, args.range]
        self.ab = args.ab
        if args.max == 'max':
            self.max = True
        if args.filename:
            if '.txt' in args.filename:
                self.filename = args.filename

    def start_minimax(self):
        m.add_arguements()
        m.read_arguements()
        input_data = m.assign_input_data()
        if input_data.get('message') is not None:
            print(input_data['message'])
            return

        parse_data = ParseData()
        root_data_obj = parse_data.get_root(self.input_graph)
        if root_data_obj["message"] is not None:
            return logging.info(root_data_obj["message"])
        self.root = root_data_obj["root"]

        nodes_data_obj = parse_data.check_node_failure(
            self.input_graph, self.leaf_nodes
        )
        if nodes_data_obj["message"] is not None:
            logging.info(nodes_data_obj["message"])

        leaves_data_obj = parse_data.check_leaf_failure(
            self.input_graph, self.leaf_nodes
        )
        if leaves_data_obj["message"] is not None:
            logging.info(leaves_data_obj["message"])

        min_max_result = self.dfs(
            node=self.root,
            is_max_player=self.max,
            alpha=float("-inf"),
            beta=float("inf"),
        )
        return f"minimax: {min_max_result}"

    def dfs(self, node, is_max_player, alpha, beta):
        if self.is_leaf(node):
            if self.range and (node < self.range[0] or node > self.range[1]):
                return float('-inf')
            return node

        if is_max_player:
            max_value = float("-inf")
            chosen_child = None

            for child in self.input_graph[node]:
                if child in self.leaf_nodes:
                    score = self.dfs(
                        self.leaf_nodes[child], False, alpha, beta
                    )
                else:
                    score = self.dfs(child, False, alpha, beta)
                if score > max_value:
                    max_value = score
                    chosen_child = child

                if self.ab:
                    alpha = max(score, alpha)
                    if beta <= alpha:
                        break

            if self.ab and beta > alpha:
                logging.info(f" max({node}) chooses {chosen_child} for {max_value}")

            if self.ab is False:
                logging.info(f" max({node}) chooses {chosen_child} for {max_value}")

            if node == self.root and self.verbose is False:
                print(f"max({self.root}) chooses {chosen_child} for {max_value}")

            return max_value
        else:
            min_value = float("inf")
            chosen_child = None
            for child in self.input_graph[node]:
                if child in self.leaf_nodes:
                    score = self.dfs(
                        self.leaf_nodes[child], True, alpha, beta
                    )
                else:
                    score = self.dfs(child, True, alpha, beta)
                if score < min_value:
                    min_value = score
                    chosen_child = child

                if self.ab:
                    beta = min(score, beta)
                    if beta <= alpha:
                        break

            if self.ab and beta > alpha:
                logging.info(f" min({node}) chooses {chosen_child} for {min_value}")

            if self.ab is False:
                logging.info(f" min({node}) chooses {chosen_child} for {min_value}")

            if node == self.root and self.verbose is False:
                print(f"min({self.root}) chooses {chosen_child} for {min_value}")
            return min_value

    def is_leaf(self, node):
        if node in self.leaf_nodes:
            return isinstance(self.leaf_nodes[node], int)
        return isinstance(node, int)


if __name__ == "__main__":
    m = Minimax()
    m.start_minimax()
