# -*- coding: UTF-8 -*-

import pymongo

## ------ Function ------
## read from a sqlite3 database
## write into a mongo db

## ------  Usage  ------
## set <path, table> from source
## set <name, collection> as destination

## Maxis @ Feb 14. Happy Valentine's Day!

def transform(src, det, server_addr='ironman.nlpweb.org'):

	## src
	import sqlitedb
	con, cur = sqlitedb.connect(src['path'])

	## det
	import pymongo
	mc = pymongo.Connection(server_addr)

	# extract columns in <src table>
	sql = 'select * from '+src['table']

	cur.execute(sql)
	res = cur.fetchone()
	columns = [x[0] for x in cur.description]
	
	# use det mongodb
	mdb = mc[det['name']]
	mdbc = mdb[det['collection']]

	# insert data from src to det
	cur.execute(sql)
	res = cur.fetchall()
	for row in res:
		data = dict(zip(columns, row))
		mdbc.insert(data)

	cur.close()
	con.close()
	return mc

def create_index(collection, columns):
	for index_columns in [ dict([(x, 1) for x in key]) for key in columns]:
		print 'creating', ' + '.join(map(lambda x:str(x), index_columns.keys()]))
		collection.ensureIndex( index_columns )

if __name__ == '__main__':

	doraemon = 'doraemon.iis.sinica.edu.tw'
	ironman = 'ironman.nlpweb.org'

	## source sqlite3 database
	# src_db_path = '/Users/Maxis/projects/scenario/TF-IDF/tf-idf.db3'
	src_db_path = '/corpus/dependency_all.db3'
	## table names from source
	src_db_tables = ['deps']

	## destination mongo db
	det_db_name = 'LJ40K'
	## destination mongo collections
	det_db_collections = ['deps']

	for (src_db_table, det_db_collection) in zip(src_db_tables, det_db_collections):
		print '> building:',src_db_path.split('/')[-1],'#',src_db_table, '-->', det_db_name,'#',det_db_collection
		mc = transform(src={'path': src_db_path, 'table': src_db_table}, det={'name': det_db_name,'collection': det_db_collection}, server_addr=doraemon)

	### create index
	columns = [['emotion', 'sentID'], ['udocID'], ['emotion']]
	create_index(mc['deps'], columns)
