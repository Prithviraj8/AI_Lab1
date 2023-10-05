class Messages():
    MULTIPLE_ROOTS = "multiple roots"
    NODE_NOT_FOUND = "node_not_found"
    LEAF_FAILURE = "leaf failure"
    VALID_ROOD = "valid_rood"

class ExceptionHandling():
    def __init__(self, input_graph):
        self.input_graph = {}

    def root_failure(self):
        visted = set()
        keys = self.input_graph.keys()
        for values in self.input_graph.values():
            for key in keys:
                if key in values and key not in visted:
                    visted.add(key)

        if len(keys) - len(visted) > 1:
            return Messages.MULTIPLE_ROOTS
        return Messages.VALID_ROOD


    def node_failure(self):
        # for parent, children in main_graph.items():
        #     parents = list()
        #     for child in children:
        #         if not isinstance(child, int):
        #             if child not in main_graph and child not in secondary_graph:
        #                 parents.append(parent)
        #     print("Child node" + child + "of" + ','.join(parents) + "not found")
        pass

    def leaf_failure(self):
        # for parent, children in main_graph.items():
        #     parents = list()
        #     for child in children:
        #         if not isinstance(child, int):
        #             if child not in main_graph and child not in secondary_graph:
        #                 parents.append(parent)
        #     print("Child node" + child + "of" + ','.join(parents) + "not found")
        pass