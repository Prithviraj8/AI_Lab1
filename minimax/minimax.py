from parse_data.parse_data import ParseData
import argparse
import logging
import sys


class Minimax():
    def __init__(self):
        self.max = False
        self.ab = False
        self.chosen_node = ""

    def add_arguements(self):

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-d', '--debug',
            help="Print lots of debugging statements",
            action="store_const", dest="loglevel", const=logging.DEBUG,
            default=logging.WARNING,
        )
        parser.add_argument(
            '-v', '--verbose',
            help="Be verbose",
            action="store_const", dest="loglevel", const=logging.INFO,
        )
        parser.add_argument(
            '-ab',
            help='Enable Alpha Beta Pruning'
        )
        parser.add_argument(
            'max',
            help='Max for the root node'
        )
        args = parser.parse_args()
        logging.basicConfig(level=args.loglevel)

    input_graph = {'a': ['b', 'c'], 'b': ['d', 'e'], 'c': ['e', 'f'], 'd': [5, 10], 'e': [10, 15], 'f': [15, 20]}

    def read_arguements(self):
        print('sys.argv: ', sys.argv)
        if 'ab' in sys.argv:
            self.ab = True

        if 'max' in sys.argv:
            self.max = True

    def start_minimax(self):
        result = self.dfs(node='a', depth=3, is_max_player=self.max, alpha=float('-inf'), beta=float('inf'))
        for key, values in self.input_graph.items():
            if result in values:
                self.chosen_node = key
                break

        if self.max is True:
            logging.info('max(a) chooses {} for {}'.format(self.chosen_node, result))
        else:
            logging.info('min(a) chooses {} for {}'.format(self.chosen_node, result))

    def dfs(self, node, depth, is_max_player, alpha, beta):

        if depth == 0 or self.is_leaf(node):
            values = [int(value) for value in self.input_graph[node]]
            print('chosen node1: ', node)
            return max(values) if is_max_player else min(values)

        if is_max_player:
            max_value = float('-inf')
            for child in self.input_graph[node]:
                max_value = max(max_value, self.dfs(child, depth - 1, False, alpha, beta))
                if self.ab:
                    alpha = max(max_value, alpha)
                    if beta <= alpha:
                        break

            return max_value
        else:
            min_value = float('inf')
            for child in self.input_graph[node]:
                min_value = min(min_value, self.dfs(child, depth - 1, True, alpha, beta))

                if self.ab:
                    beta = min(min_value, beta)
                    if beta >= alpha:
                        break
            return min_value

    def is_leaf(self, node):
        # TODO: improve check for leaf. Loop over all chidlren of the given node to check if there's one integer.
        #  That'll be a leaf.
        for children in self.input_graph[node]:
            if isinstance(children, int):
                return True
        return False
        # return node not in self.input_graph or len(self.input_graph[node]) == 2


if __name__ == '__main__':
    m = Minimax()
    m.add_arguements()
    m.read_arguements()
    m.start_minimax()
    # print('ans: ', m.dfs(node='a', depth=3, is_max_player=False, alpha=float('-inf'), beta=float('inf')))
