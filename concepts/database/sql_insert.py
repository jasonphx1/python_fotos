#!/usr/bin/env python3

__author__ = "Jason Lutz"

import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ?)', ('Thunderstruck', 20) )
cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ?)', ('MyWay ', 15) )

conn.commit()

print("Tracks:")
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

