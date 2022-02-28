from py2neo import Graph

def parse_target(t:str):
	e = [i.upper() for i in t.split("/")]
	e.reverse()
	return '@'.join(e)

def list_localadmin(graph: Graph, options):
    req = graph.run("""MATCH p=(m:User {name: "%s"})-[r:AdminTo]->(n:Computer)
			   RETURN DISTINCT n.name, n.operatingsystem
			   ORDER BY n.name""" % parse_target(options.target)).to_table()

    for i in req:
        print('%s,%s' % i)