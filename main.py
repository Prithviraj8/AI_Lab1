# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.

def root_exists():
    input_graph = {'a': ['a1', 'a2', 'a3'], 'a1': [-4, 3], 'a3': [-1, 8], 'a2': [5, 2]}
    visted = set()
    keys = input_graph.keys()
    for values in input_graph.values():
        for key in keys:
            if key in values and key not in visted:
                visted.add(key)

    if len(input_graph.keys()) - len(visted) > 1:
        print('No Root')
    else:
        print('Root')


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    root_exists()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
