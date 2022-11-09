from pymongo import MongoClient
import base64
import pytesseract
from weak_classifier import classify
import os
import multiprocessing
import json

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
        if j['class'] == "BED SIDE PROCEDURE" or j['class'] == j['class'] == "TRIAGE DOCUMENT" or j[
            'class'] == "Pediatric Early Warning Score" or j['class'] == "NEUROLOGICAL ASSESSMENT" or j[
            'class'] == "INITIAL NURSING ASSESSMENT" or j['class'] == "GRAPHICAL ASSESSMENT" or j[
            'class'] == "GRAPHIC CHART" or j['class'] == "MODIFIED GLASGOW COMA SCALE":
            df.update_one({'_id': mongo_id}, {"$set": {"main_type": "EMERGENCY DOCUMENTS"}}, upsert=True)
        elif j['class'] == "OLD FACE SHEET" or j['class'] == "CONSENT FORM" or j['class'] == "FACE SHEET":
            df.update_one({'_id': mongo_id}, {"$set": {"main_type": "PATIENT INFORMATION AND CONSENT"}}, upsert=True)
        elif j['class'] is None:
            df.update_one({'_id': mongo_id}, {"$set": {"main_type": "NO"}}, upsert=True)
        else:
            df.update_one({'_id': mongo_id}, {"$set": {"main_type": "PATIENT HISTORY"}}, upsert=True)


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


def get_images_viewer_op(mr, date, doc_id):
    bsp = []
    tds = []
    pewss = []
    nas = []
    inas = []
    gas = []
    gcs = []
    mgcss = []

    ofcs = []
    cfs = []
    fcs = []
    my_client = MongoClient(connect=False)
    my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))
    collection = my_client["DOC_SCAN"]
    df = collection['DOCUMENTS']
    bp = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id, "class": "BED SIDE PROCEDURE"})
    for i in bp:
        bsp.append({"base64": str(bp["doc"])})
    td = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                  "class": "TRIAGE DOCUMENT"})
    for i in td:
        tds.append({"base64": str(bp["doc"])})
    pews = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                    "class": "Pediatric Early Warning Score"})
    for i in pews:
        pewss.append({"base64": str(bp["doc"])})
    na = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                  "class": "NEUROLOGICAL ASSESSMENT"})
    for i in na:
        nas.append({"base64": str(bp["doc"])})
    ina = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                   "class": "INITIAL NURSING ASSESSMENT"})
    for i in ina:
        inas.append({"base64": str(bp["doc"])})
    ga = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                  "class": "GRAPHICAL ASSESSMENT"})
    for i in ga:
        gas.append({"base64": str(bp["doc"])})
    gc = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                  "class": "GRAPHIC CHART"})
    for i in gc:
        gcs.append({"base64": str(bp["doc"])})
    mgcs = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                    "class": "MODIFIED GLASGOW COMA SCALE"})
    for i in mgcs:
        mgcss.append({"base64": str(bp["doc"])})
    ofc = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                   "class": "OLD FACE SHEET"})
    for i in ofc:
        ofcs.append({"base64": str(bp["doc"])})
    cf = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                  "class": "CONSENT FORM"})
    for i in cf:
        cfs.append({"base64": str(bp["doc"])})
    fc = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                  "class": "FACE SHEET"})
    for i in fc:
        fcs.append({"base64": str(bp["doc"])})
    fc = df.find({"mrno": mr, "visit_date_op": date, "doctor_id_ip": doc_id,
                  "class": "FACE SHEET"})
    for i in fc:
        fcs.append({"base64": str(bp["doc"])})

    returning_object = {
        {
            "name": "EMERGENCY DOCUMENTS",
            "id": "XXXQ01",
            "TRIAGE DOCUMENT": tds,
            "Pediatric Early Warning Score": pewss,
            "NEUROLOGICAL ASSESSMENT": nas,
            "INITIAL NURSING ASSESSMENT": inas,
            "GRAPHICAL ASSESSMENT": gas,
            "GRAPHIC CHART": gcs,
            "MODIFIED GLASGOW COMA SCALE": mgcss,
        },
        {
            "name": "EMERGENCY DOCUMENTS",
            "id": "XXXQ02",
            "OLD FACE SHEET": ofcs,
            "CONSENT FORM": cfs,
            "FACE SHEET": fcs
        }
    }
    return returning_object


def bring_users_data():
    my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))
    collection = my_client["DOC_SCAN"]
    doc_id = collection['VIEWER_AUTH']
    cursor = doc_id.find({})
    data = []
    for document in cursor:
        data.append(document)
    res = {
        "data": data,
        "status": 1,
        "msg": "Success"
    }
    return res


if __name__ == '__main__':
    get_multi_vector_single_using_te()
