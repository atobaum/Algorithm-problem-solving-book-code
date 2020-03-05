import graphviz

class visualization:
    def __init__(self, root, leftFn, rightFn, valFn):
        self.__r = root
        self.__lfn = leftFn
        self.__rfn = rightFn
        self.__vfn = valFn
    
    def draw(self):
        g = graphviz.Digraph(format = 'png')
        self.__init(g, self.__r, 'r')
        g.render(view=True)
    
    def __init(self, g, node, node_idx):
        g.node(node_idx, self.__vfn(node))

        if self.__lfn(node) is not None:
            self.__init(g, self.__lfn(node), node_idx+'l')
            g.edge(node_idx, node_idx+'l')
        if self.__rfn(node) is not None:
            self.__init(g, self.__rfn(node), node_idx+'r')
            g.edge(node_idx, node_idx+'r')