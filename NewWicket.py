
from Date import *
from CURSOR import *
from vid import *
import uuid

wicket_ID = None
def data_inputs(corsor):
    global wicket_ID
    INPUT = input("create new block? Y/N")
    if INPUT == 'Y':
        date = date_check()
        bowler = input("bowler name")
        bowler_team = input("bowler team")
        batsman = input("batsman")
        batsman_team = input("batsman team")
        runs = int(input("Enter the number of runs (score) there was when wicket was taken"))
        # wicket number ki valdation or input
        flag = False
        while not flag:
            wicket_number = int(input("What number of the wicket was it in the match"))
            if wicket_number >= 11 or wicket_number <= 0:
                print("wrong wicket number")
            else:
                flag = True

        venue_country = input("just name the venue or stadium")
        # vid ka kam
        file = input("file name please and path please")
        vid = vidhasher(file)
        # block ka ID
        wicket_ID = str(uuid.uuid4())

        corsor.execute("""INSERT INTO WICKETS(ID, Date, Bowler, Bowler_team, Batsman_team, runs, wickets, venue_country, batsman, Vid)
        VALUES (?,?,?,?,?,?,?,?,?,?)""",
                       (wicket_ID, date, bowler, bowler_team, batsman_team, runs, wicket_number, venue_country, batsman,
                        vid))


