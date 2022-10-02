from pymongo import MongoClient
import base64
import pytesseract
from weak_classifier import classify
import os

pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'


def get_multidimentional_vector_single():
    my_client = MongoClient(connect=False)
    my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))
    collection = my_client["DOC_SCAN"]
    df = collection['DOCUMENTS']
    q = df.find({"ocr": None})
    # for i in q:
    #     df.update_one({"ocr": None}, {"$set": {"ocr": ""}})
    for j in q:
        img = j["doc"]
        name = str(j["doc_id"]) + ".jpg"
        # with open(name, "wb") as fh:
        #     fh.write(base64.decodebytes(img))
        f = open(name, 'wb')
        f.write(img)
        f.close()
        df.update_one({"doc_id": str(j["doc_id"])}, {"$set": {"ocr": classify(name)}})
        os.remove(name)


if __name__ == '__main__':
    get_multidimentional_vector_single()
