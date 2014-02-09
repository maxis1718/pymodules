# -*- coding: utf-8 -*-

import sqlite3

def connect(db_path):
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	return (con, cur)