import cx_Oracle
import pandas as pd
from pymongo import MongoClient


def clone_mongo():
    my_client = MongoClient()
    my_client = MongoClient('localhost', 27017)
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
