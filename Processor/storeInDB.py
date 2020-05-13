# Not needed. Will be removed

import pymongo
from Database import Mongo

def storeInMongo(chunks):

    db = Mongo()
    dbname = db["data"]
    dbcol = dbname["processed_data"]
    print(db.getAllDB())
    x = dbcol.insertInto(dbname, dbcol, chunks)
    print(x.inserted_ids)

class storeInDB():
    pass
