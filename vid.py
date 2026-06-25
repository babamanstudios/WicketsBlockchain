import hashlib
from CURSOR import *

def vidhasher(path):
    hash = hashlib.sha256()
    with open(path, "rb") as video:
        while part := video.read(1024):
            hash.update(part)
    return hash.hexdigest()

def old_vid(wicket_id):
    curser = define_cursor(start())
    curser.execute(""" SELECT VID
    FROM WICKETS
        WHERE ID = ?""", (wicket_id,))  # database se vid otaya
    vidd = curser.fetchone()[0]  # vidd mein store
    stop(start())
    return vidd



def vid_validation(Old_vid,new_vid,wicket_id):
    curser = define_cursor(start())
    if Old_vid != new_vid:
        print("failed")
        curser.execute("DELETE FROM WICKETS WHERE ID = ?", (wicket_id,))
    else:
        print("passed")
    stop(start())
