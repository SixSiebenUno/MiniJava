from graphviz import Digraph

dot = Digraph(comment='Tree')

dot.node('A', 'Dot A')
dot.node('B', 'Dot B')
dot.node('C', 'Dot C')
dot.node('D', 'Dot D')
dot.node('E', 'Dot E')
dot.node('F', 'Dot F')
dot.node('G', 'Dot G')

dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'E')
dot.edge('C', 'D')
dot.edge('C', 'F')
dot.edge('F', 'G')

dot.format = 'png'
dot.render('tree.gv', view=True)