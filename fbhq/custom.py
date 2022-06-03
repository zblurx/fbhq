from py2neo import Graph

def custom(graph: Graph, options):
	req = graph.run(options.query).to_table()
	for i in req:
		for j in i:
			print('%s' % j, end=' ')
		print()