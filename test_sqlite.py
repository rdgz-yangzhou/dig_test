#!/usr/bin/env pypy

import sqlite3
import os,sys


def test_sql():
	try:
		sql = sqlite3.connect("./test.db")
	except Exception,e:
		sql = None
	if sql is None:
		return
	cursor = sql.cursor()
	cursor.execute("create table if not exists catalog (id integer primary key, pid integer, name varchar(10) UNIQUE)")
	cursor.execute("insert into catalog values(1, 0, 'hello')");
	cursor.execute("insert into catalog values(0, 0, 'name1')")
	sql.commit()
	cursor.execute("select * from catalog");
	print cursor.fetchall()
	cursor.close()
	sql.close()
	pass

if __name__ ==  "__main__" :
	test_sql()
