import cx_Oracle
import pandas as pd
from pymongo import MongoClient
import multiprocessing


def clone_mongo():
    while True:
        my_client = MongoClient(connect=False)
        my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))
        collection = my_client["DOC_SCAN"]
        doc_id = collection['AUTH']
        doc_id.drop()

        dsn_tns = cx_Oracle.connect('ASAD_25510/asad#123@prodhims.shifa.com.pk:1521/himsdb.shifa.com.pk')
        cursor = dsn_tns.cursor()

        query = "select cdr.api_users.username , cdr.api_users.password  from cdr.api_users"

        for row in cursor.execute(query):
            df = pd.DataFrame(row, index=["USERNAME", "PASSWORD"], )
            # print(df)
            result = {
                "USERNAME": df.iloc[0][0],
                "PASSWORD": df.iloc[1][0]
            }
            doc_id.insert_one(result)


def initiate_mongo_devil():
    cm = multiprocessing.Process(target=clone_mongo, daemon=True)
    cm.start()
