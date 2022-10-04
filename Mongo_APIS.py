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
    tm = multiprocessing.Process(target=get_multi_vector_single_using_te, daemon=True)
    tm.start()


def looper():
    while True:
        get_multi_vector_single_using_te()


def get_by_mr(mrno, type):
    return_obj = []
    my_client = MongoClient(connect=False)
    my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))
    collection = my_client["DOC_SCAN"]
    df = collection['DOCUMENTS']
    return_obj = []
    if type == "XXQ01":
        q = df.find({"class": "BED SIDE PROCEDURE", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ02":
        q = df.find({"class": "MODIFIED GLASGOW COMA SCALE", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ03":
        q = df.find({"class": "INITIAL NURSING ASSESSMENT", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ04":
        q = df.find({"class": "PEWS", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ05":
        q = df.find({"class": "GRAPHICAL ASSESSMENT", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ06":
        q = df.find({"class": "GRAPHICAL CHART", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ07":
        q = df.find({"class": "NEUROLOGICAL ASSESSMENT", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ08":
        q = df.find({"class": "TRIAGE DOCUMENT", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ09":
        q = df.find({"class": "AUTHORIZATION AND CONSENT FORM", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ10":
        q = df.find({"class": "FACE SHEET", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ11":
        q = df.find({"class": "PATIENT MEDICAL RECORD", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ12":
        q = df.find({"class": "PATIENT REGISTRATION FORM", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ13":
        q = df.find({"class": "HISTORY AND PHYSICAL", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ14":
        q = df.find({"class": "NURSING ASSESSMENT", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj
    elif type == "XXQ15":
        q = df.find({"class": "PHYSICIAN PROGRESS RECORD", "mrno": str(mrno)})
        for j in q:
            img = j["doc"]
            return_obj.append({"base64": img})
            return return_obj


if __name__ == '__main__':
    print(get_by_mr("228897", "XXQ15"))
