from fbhq.custom import custom
from fbhq.list_localadmin import list_localadmin

from py2neo import Graph
import argparse

def main():
	parser = argparse.ArgumentParser(description="Fast BloodHound Queries")
	parser.add_argument('-b', '--bolt', type=str, default="bolt://127.0.0.1:7687", help="Neo4j bolt connexion (default: bolt://127.0.0.1:7687)")
	parser.add_argument('-u', '--username', type=str, default="neo4j", help="Neo4j username (default : neo4j)")
	parser.add_argument('-p', '--password', type=str, default="neo4j",help="Neo4j password (default : neo4j)")

	subparsers = parser.add_subparsers(help="Action", dest="action", required=True)

	list_localadmin_parser = subparsers.add_parser("list-localadmin", help="List where user is local admin")
	list_localadmin_parser.add_argument(
		'-t',
		'--target',
		type=str, 
		required=True,
		help="Domain user in form of waza.local/Administrator"
	)

	custom_parser = subparsers.add_parser("custom", help="Custom bloodhound query, with result in terminal")
	custom_parser.add_argument(
		'query',
		action='store',
		help="Custom bloodhound query"
	)

	args = parser.parse_args()
	try:
		g = Graph(args.bolt, auth=(args.username, args.password))
	except Exception as e:
		print(e)
		exit(0)

	if args.action == "list-localadmin":
		list_localadmin(g, args)
	if args.action == "custom":
		custom(g, args)
	else:
		raise Exception("Action not implemented: %s" % args.action)

if __name__ == "__main__":
    main()