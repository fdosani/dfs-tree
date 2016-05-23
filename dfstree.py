"""
DFS algorithim of a basic Tree structure
"""

class Tree(object):
    """Basic Tree object to hold the data and a list representing the
    children
    """
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    @staticmethod
    def dfsearcher(tree, node):
        """
        basic depath first searcher which will recursively go through a tree
        and check each node. If it finds the node which is asked for it will
        return it, otherwsie it will return None
        """
        #if the current item is the node we are looking for then return it.
        print "Currently on node: {0}".format(tree.data)
        if tree.data == node:
            return tree.data
        #if no children then backtrack by returning None
        elif len(tree.children) == 0:
            return None
        #children exist and we want go down into the tree
        else:
            for t in tree.children:
                subtree = Tree.dfsearcher(t, node)
                if subtree == node:
                    return subtree







"""
        a
       / \
      b   c
     /|\   \
    d e f   g
            |
            h
Lets implement the following tree and search for items using DFS
"""

if __name__ == '__main__':
    my_tree = Tree("a",
                [Tree("b",[Tree("d"),
                           Tree("e"),
                           Tree("f"),]),
                 Tree("c",[Tree("g",[Tree("h")])])
                ])
    result = Tree.dfsearcher(my_tree, "h")
    print "Search results: {0}".format(result)
