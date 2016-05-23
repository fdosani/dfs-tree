# dfs-tree

Basic implementation of a Tree class:

```
Tree class
|-----> data (string)
|-----> children (list of Trees)

```

The class implements a `staticmethod` which accepts a `Tree` and a node to
search for.

It will either return a node (data) which you were looking for or `None`

### Uasge
```
python dfstree.py
```

You can alter the predefined tree by changing the `my_tree` variable
```
my_tree = Tree("a",
            [Tree("b",[Tree("d"),
                       Tree("e"),
                       Tree("f"),]),
             Tree("c",[Tree("g",[Tree("h")])])
            ])
```
