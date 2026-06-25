from CURSOR import *

start()
cersur = define_cursor(start())


cersur.execute(""" CREATE TABLE IF NOT EXISTS WICKETS (
ID TEXT primary key NOT NULL,
Date TEXT,
Bowler TEXT,
Bowler_team TEXT,
Batsman_team TEXT,
runs INTEGER,
wickets INTEGER,
venue_country TEXT,
batsman TEXT,
Vid TEXT
)""")

stop(start())