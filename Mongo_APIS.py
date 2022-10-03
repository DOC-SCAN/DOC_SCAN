from pymongo import MongoClient
import base64
import pytesseract
from weak_classifier import classify
import os
import multiprocessing

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'


def get_multi_vector_single_using_te():
    my_client = MongoClient(connect=False)
    my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))
    collection = my_client["DOC_SCAN"]
    df = collection['DOCUMENTS']
    q = df.find({"ocr": None})
    # for i in q:
    #     df.update_one({"ocr": None}, {"$set": {"ocr": ""}})
    for j in q:
        img = j["doc"]
        mongo_id = j["_id"]
        name = str(j["doc_id"]) + ".jpg"
        f = open(name, 'wb')
        f.write(img)
        f.close()
        df.update_one({'_id': mongo_id}, {"$set": {"class": classify(name)}}, upsert=True)
        os.remove(name)


def initiate_tes_devil():
    tm = multiprocessing.Process(target=get_multi_vector_single_using_te(), daemon=True)
    tm.start()


if __name__ == '__main__':
    get_multi_vector_single_using_te()
