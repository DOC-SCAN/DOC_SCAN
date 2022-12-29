from pymongo import MongoClient

my_client = MongoClient()
my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))

db = my_client["DOC_SCAN"]
collection = db['DOCUMENTS']

total_files = collection.distinct('mrno')
total_documents = collection.count_documents({})
total_unclassified = collection.count_documents({"class": "0"})
current_classifier_accuracy = 100 - ((total_unclassified/total_documents)*100)
total_classified = total_documents - total_unclassified
total_space_used = db.command("")

if __name__ == '__main__':
    print(len(total_files))
    print(total_documents)
    print(total_unclassified)
    print(round(current_classifier_accuracy, 2))
    print(total_classified)

