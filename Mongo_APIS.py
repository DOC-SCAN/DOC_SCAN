from pymongo import MongoClient
import base64
import pytesseract
from weak_classifier import classify
import os
import multiprocessing
import json
import bson
import base64

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
    cursor = doc_id.find({}, {'_id': False,
                              'PASSWORD': False,
                              'password_changed': False,
                              'total_images_scanned': False,
                              })
    data = []
    for document in cursor:
        data.append(document)
    res = {
        "data": data,
        "status": 1,
        "msg": "Success"
    }
    return res


def bulk_viewer(mr_no):
    mr = mr_no
    my_client = MongoClient()
    my_client = MongoClient(host='mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'),
                            unicode_decode_error_handler='ignore')
    collection = my_client["DOC_SCAN"]
    doc_id = collection['AUTH']
    doc = collection['DOCUMENTS']

    cur = doc.find({"mrno": mr})
    a0 = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    a8 = []
    a9 = []
    a10 = []
    a11 = []
    a12 = []
    a13 = []
    a14 = []

    for document in cur:
        if not document['is_del']:
            if document['class'] == '1':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a0.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '2':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a1.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '3':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a2.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '4':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a3.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '5':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a4.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '6':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a5.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '7':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a6.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '8':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a7.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '9':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a8.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '10':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a9.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '11':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a10.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '12':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a11.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '13':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a12.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '14':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a13.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
            elif document['class'] == '0':
                img = document['doc']
                f = open("tmp.jpg", "wb")
                f.write(img)
                f.close()
                with open("tmp.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                a14.append({'base64': encoded_string.decode('utf-8'), 'id': document['doc_id']})
                os.remove('tmp.jpg')
        obj = {
            "data": [{
                "id": 1,
                "image": a0
            },
                {
                    "id": 2,
                    "image": a1
                },
                {
                    "id": 3,
                    "image": a2
                },
                {
                    "id": 4,
                    "image": a3
                },
                {
                    "id": 5,
                    "image": a4
                },
                {
                    "id": 6,
                    "image": a5
                },
                {
                    "id": 7,
                    "image": a6
                },
                {
                    "id": 8,
                    "image": a7
                },
                {
                    "id": 9,
                    "image": a8
                },
                {
                    "id": 10,
                    "image": a9
                },
                {
                    "id": 11,
                    "image": a10
                },
                {
                    "id": 12,
                    "image": a11
                },
                {
                    "id": 13,
                    "image": a12
                },
                {
                    "id": 14,
                    "image": a13
                },
                {
                    "id": 0,
                    "image": a14
                }],
            "status": 200,
            "message": "Success"
        }
    return obj


def soft_del(doc_idd):
    my_client = MongoClient()
    my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))

    db = my_client["DOC_SCAN"]
    collection = db['DOCUMENTS']
    doc_to_del = collection.update_one({"doc_id": doc_idd}, {"$set"  : {"is_del": True}})


if __name__ == '__main__':
    get_multi_vector_single_using_te()
