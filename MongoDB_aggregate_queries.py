'''
Created on Jan 3, 2016
@author: hanhanwu
aggregates queries
'''
import pymongo


def main():
    client = pymongo.MongoClient()
    db = client.enron
    
    # recipients per message
    recipients_per_msg_cursor = db.mbox.aggregate([
                            {'$match': {'From': 'kenneth.lay@enron.com'}}, 
                            {'$project': {'From': 1, 'To': 1}},
                            {'$group': {'_id': '$From', 'recipients': {'$addToSet': '$To'}}}
                            ])
    
    # convert cursor object into a list so that we can access the data                        
    recipients_per_msg = list(recipients_per_msg_cursor)[0]['recipients']
    num_recipients_per_message = sorted([len(recipients) for recipients in recipients_per_msg])
    print 'num of recipients per message: ', num_recipients_per_message
    
    # merge all the recipients into 1 list
    all_recipients = [recipient for recipients in recipients_per_msg for recipient in recipients]
    print 'all recipients: ', len(all_recipients)
    
    unique_recipients_cursor = db.mbox.aggregate([
                            {'$match': {'From': 'kenneth.lay@enron.com'}}, 
                            {'$project': {'From': 1, 'To': 1}},
                            {'$unwind': '$To'},
                            {'$group': {'_id': '$From', 'recipients': {'$addToSet': '$To'}}}
                            ])
    unique_recipients = list(unique_recipients_cursor)[0]['recipients']
    print 'num of unique recipients: ', len(unique_recipients)
    
if __name__ == '__main__':
    main()
