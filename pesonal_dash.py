from pymongo import MongoClient
from MONGO_CRED import DB_URL, DB_PASSWORD, DB_USERNAME

my_client = MongoClient()
my_client = MongoClient(DB_URL % (DB_USERNAME, DB_PASSWORD))

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
    print(stats_calculator())
