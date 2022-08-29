from pymongo import MongoClient

my_client = MongoClient()
my_client = MongoClient('localhost', 27017)


def doc_id_dispatcher():
    collection = my_client["DOC_SCAN"]
    doc_id = collection['DOCUMENT_ID']
    t = doc_id.find_one()
    ret = t["doc_id"]

    doc_id.update_one({'doc_id': ret}, {'$set': {'doc_id': ret + 1}})
    return ret


def doc_saver():
    pass

# added this to push without ssl



