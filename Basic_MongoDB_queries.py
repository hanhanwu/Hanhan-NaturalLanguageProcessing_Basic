'''
Created on Jan 3, 2016
@author: hanhanwu
using python to access MongoDB
'''
import json
import pymongo
from bson import json_util
from datetime import datetime as dt

# query the data within a date range and sort by date
def sort_by_date():
    client = pymongo.MongoClient()
    db = client.enron
    mbox = db.mbox
    
    start_date = dt(2001, 10, 1)
    end_date = dt(2001, 10, 2)
    
    msgs = [msg for msg in mbox.find({'Date':
                                      {
                                       '$lt': end_date,
                                       '$gt': start_date
                                       }
                                      }).sort('date')]
    print json.dumps(msgs, indent=1, default=json_util.default)
    
def count_users():
    client = pymongo.MongoClient()
    db = client.enron
    mbox = db.mbox
    senders = [sender for sender in mbox.distinct('From')]
    receivers = [receiver for receiver in mbox.distinct('To')]
    cc_receivers = [c for c in mbox.distinct('Cc')]
    bcc_receivers = [bcc for bcc in mbox.distinct('Bcc')]
    
    print 'senders: ', len(senders)
    print 'receivers: ', len(receivers)
    print 'Cc: ', len(cc_receivers)
    print 'Bcc: ', len(bcc_receivers)
    
    senders_set = set(senders)
    receivers_set = set(receivers)
    cc_receivers_set = set(cc_receivers)
    bcc_receivers_set = set(bcc_receivers)
    
    common_sender_receivers = senders_set.intersection(receivers_set)
    all_receivers = receivers_set.union(cc_receivers_set).union(bcc_receivers_set)
    senders_not_receivers = senders_set.difference(receivers_set)
    
    print len(common_sender_receivers)
    print len(all_receivers)
    print len(senders_not_receivers)
    
    # close specification using $in
    possible_alias = ['kenneth.lay@enron.com', 'ken_lay@enron.com', 'ken.lay@enron.com',
                      'klay@enron.com', 'kenneth.lay@enron.net']
    to_msgs = [m for m in mbox.find({'To': {'$in': possible_alias}})]
    from_msgs = [m for m in mbox.find({'From': {'$in': possible_alias}})]
    
    print 'possible CEO to: ', len(to_msgs)
    print 'possible CEO from: ', len(from_msgs)
    
    # count enron employees using key_words
    employee_senders = [s for s in mbox.distinct('From') if s.lower().find('@enron.com')>0]
    print len(employee_senders)
    print employee_senders[0]
    

def main():
    count_users()
    
if __name__ == '__main__':
    main()
