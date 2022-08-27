from pymongo import MongoClient

myclient = MongoClient()
myclient = MongoClient('localhost', 27017)


def get_doc_id():
    collection = myclient["DOC_SCAN"]
    doc_id = collection['DOCUMENT_ID']
    t = doc_id.find_one()
    ret = t["doc_id"]

    doc_id.update_one({'doc_id': ret}, {'$set': {'doc_id': ret + 1}})
    return ret


if __name__ == '__main__':
    get_doc_id()
