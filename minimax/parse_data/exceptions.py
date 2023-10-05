class Messages:
    MULTIPLE_ROOTS = "multiple roots"
    NODE_NOT_FOUND = "node_not_found"
    LEAF_FAILURE = "leaf failure"
    VALID_ROOD = "valid_rood"


class ExceptionHandling:
    def root_failure(self, input_graph):
        result = {"root": None, "message": None}
        visited = set()
        keys = input_graph.keys()
        for values in input_graph.values():
            for key in keys:
                if key in values and key not in visited:
                    visited.add(key)

        if len(keys) - len(visited) > 1:
            result["message"] = f"multiple roots: {set(keys) - visited}"
            return result
        root = None
        for key in keys:
            if key not in visited:
                root = key
                break
        result["root"] = root
        return result

    def node_failure(self, input_graph, leaf_nodes):
        result = {"message": None}
        for parent, children in input_graph.items():
            parents = []
            for child in children:
                if not isinstance(child, int):
                    if child not in input_graph and child not in leaf_nodes:
                        parents.append(parent)
            if parents:
                result[
                    "message"
                ] = f"Child node: {child} of {','.join(parents)} not found"
                break
        return result

    def leaf_failure(self, input_graph, leaf_nodes):
        result = {"message": None}
        for parent, children in input_graph.items():
            parents = []
            for child in children:
                if child not in input_graph and child not in leaf_nodes:
                    parents.append(parent)
            if parents:
                result[
                    "message"
                ] = f"Child node: {child} of {','.join(parents)} not found"
                break
            if parents:
                result[
                    "message"
                ] = f"Child node: {child} of {','.join(parents)} not found"
                break
        return result


if __name__ == "__main__":
    ex = ExceptionHandling(
        {
            "a": ["b", "c"],
            "b": ["d", "e"],
            "c": ["e", "f"],
            "d": [5, 10],
            "e": [10, 15],
            "f": [15, 20],
        }
    )
    print(ex.root_failure())
