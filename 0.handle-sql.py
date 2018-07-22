from pprint import pprint
import sqlite3

conn = sqlite3.connect('tl.db')
c = conn.cursor()

c.execute('''
        SELECT Message FROM Message
        ''')

r = c.fetchall()
pprint(r)
