'''
Created on Jan 4, 2016
@author: hanhanwu
using  MongoDB indexing
key word search using indexing, aggregate
'''
import json
import pymongo
from bson import json_util

def main():
    client = pymongo.MongoClient()
    db = client.enron
    mbox = db.mbox
    
    # Create an index, if the index already exists, it's still fine to run this code. 
    # $** means the index for all fields, 'text' is the index type, 'TextIndex' is the index name.
    mbox.create_index([('$**', 'text')], name = 'TextIndex', type = 'text')
    
    # get the collaction stats (collstats) on a collection (mbox)
    print json.dumps(db.command('collstats', 'mbox'), indent = 1)
    
    # using indexing to search for keywords, issue a text command
    # json_util is used for the serialization of JSON
    print json.dumps(db.command("text", "mbox", search = "raptor", limit = 1),
                     indent = 1,
                     default = json_util.default
                     )
    
    # using aggregate to search for keywords, and gather the content from those emails which contain the keyword
    key_wrods_cursor = db.mbox.aggregate([
                            {'$match': {'$text': {'$search': 'raptor'}}}
                            ])
      
    results = list(key_wrods_cursor)
    results = [result['part'][0]['content'] for result in results]

    # using indexing to search for keywords, with find() method
    find_results_cursor = mbox.find({ '$text': { '$search': "raptor" } })
    find_results = list(find_results_cursor)
    find_results = [result['part'][0]['content']for result in find_results]
    print len(find_results)
    print find_results[0]

    
if __name__ == '__main__':
    main()
