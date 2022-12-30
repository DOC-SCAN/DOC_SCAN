from pymongo import MongoClient

my_client = MongoClient()
my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))

db = my_client["DOC_SCAN"]
collection = db['DOCUMENTS']


def stats_calculator():
    total_files = collection.distinct('mrno')
    total_documents = collection.count_documents({})
    total_unclassified = collection.count_documents({"class": "0"})
    current_classifier_accuracy = 100 - ((total_unclassified / total_documents) * 100)
    total_classified = total_documents - total_unclassified
    total_space_used = db.command("collstats", "DOCUMENTS")
    total_space_used = total_space_used['size']
    total_space_used = total_space_used / 1000000000

    stats = {
        "files": len(total_files),
        "documents": total_documents,
        "unclassified": total_unclassified,
        "classified": total_classified,
        "space_used": total_space_used,
    }
    return stats


if __name__ == '__main__':
    pass
