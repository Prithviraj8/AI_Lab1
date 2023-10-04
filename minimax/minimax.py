import argparse
import logging
import sys

from parse_data.parse_data import ParseData


class Minimax:
    def __init__(self):
        self.max = False
        self.ab = False
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
        parser.add_argument("-ab", help="Enable Alpha Beta Pruning")
        parser.add_argument("max", help="Max for the root node")
        # parser.add_argument("min", help="Min for the root node")
        args = parser.parse_args(sys.argv)
        logging.basicConfig(level=args.loglevel)

    def get_input_data(self):
        parse_data = ParseData()
        input_data = parse_data.get_input_data("input_file")
        print("input_data: ", input_data)
        self.input_graph = input_data["input_graph"]
        self.tree_depth = input_data["tree_depth"]
        self.leaf_nodes = input_data['leaf_nodes']

    def read_arguements(self):
        print('arguements: ', sys.argv)
        if "-ab" in sys.argv:
            self.ab = True

        if "max" in sys.argv:
            self.max = True

    # TODO:: pass the root here correctly rather than assuming its 'a'
    def get_chosen_node(self, result, root='a'):
        parent_chosen_node = None
        child_chosen_node = None
        for key, values in self.input_graph.items():
            if result in values:
                child_chosen_node = key
                break

        for key, values in self.input_graph.items():
            if child_chosen_node in values:
                parent_chosen_node = key

        if parent_chosen_node == root:
            return child_chosen_node
        return parent_chosen_node

    def start_minimax(self):
        result = self.dfs(
            node="a",
            depth=self.tree_depth,
            is_max_player=self.max,
            alpha=float("-inf"),
            beta=float("inf"),
        )
        chosen_node = self.get_chosen_node(result)

        if self.max is True:
            logging.info("max(a) chooses {} for {}".format(chosen_node, result))
        else:
            logging.info("min(a) chooses {} for {}".format(chosen_node, result))

    def dfs(self, node, depth, is_max_player, alpha, beta):
        if depth == 0 or self.is_leaf(node):
            values = [int(value) for value in self.input_graph[node]]
            print("chosen node1: ", node)
            if is_max_player:
                value = max(values)
                for node, values in self.input_graph.items():

                for leaf_node, node_value in self.leaf_nodes.items():
                    if value == node_value:
                        logging.info('max({}) chooses {} for {}'.format(node, leaf_node, node_value))
                        break
            else:
                value = min(values)
                for leaf_node, node_value in self.leaf_nodes.items():
                    if value == node_value:
                        logging.info('min({}) chooses {} for {}'.format(node, leaf_node, node_value))
                        break

            return value

        print('is_ab: ', self.ab)
        if is_max_player:
            max_value = float("-inf")
            for child in self.input_graph[node]:
                max_value = max(
                    max_value, self.dfs(child, depth - 1, False, alpha, beta)
                )
                if self.ab:
                    alpha = max(max_value, alpha)
                    if beta <= alpha:
                        logging.info('alpha pruning: {} for the node: {}'.format(max_value, node))
                        break
            return max_value
        else:
            min_value = float("inf")
            for child in self.input_graph[node]:
                min_value = min(
                    min_value, self.dfs(child, depth - 1, True, alpha, beta)
                )

                if self.ab:
                    beta = min(min_value, beta)
                    if beta >= alpha:
                        logging.info('beta pruning: {} for the node: {}'.format(min_value, node))
                        break
            return min_value

    def is_leaf(self, node):
        # TODO: improve check for leaf. Loop over all chidlren of the given node to check if there's one integer.
        #  That'll be a leaf.
        for children in self.input_graph[node]:
            if isinstance(children, int):
                return True
        return False


if __name__ == "__main__":
    m = Minimax()
    m.add_arguements()
    m.read_arguements()
    m.get_input_data()
    m.start_minimax()
