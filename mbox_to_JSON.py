'''
Created on Jan 1, 2016
@author: hanhanwu
convert mbox format to the JSON format that fits MangoDB
'''
import json
import quopri
import time
import mailbox
import email
from bs4 import BeautifulSoup
from dateutil.parser import parse


# When using a generator, it requires a trivial encoder to be passed to json for object serialization
class Encoder(json.JSONEncoder):
    def default(self, o):
        return list(o)
    
# decode the "quote printable" format and strip out the HTML tags
def clean_msg(msg):
    msg = quopri.decodestring(msg)
    try:
        soup = BeautifulSoup(msg)
    except:
        return ''
    return ''.join(soup.findAll(text = True))

def jsonifyMsg(msg):
    json_msg = {'part': []}
    for k, v in msg.items():
        json_msg[k] = v.decode('utf-8', 'ignore')
        
    for k in ['To', 'Cc', 'Bcc']:
        if not json_msg.get(k):
            continue
        json_msg[k] = json_msg[k].replace('\n', '').replace('\t', '').replace('\r', '')\
                                 .replace(' ', '').decode('utf-8', 'ignore').split(',')
                                 
    for part in msg.walk():
        json_part = {}
        if part.get_content_maintype() == 'multipart':
            continue
        json_part['contentType'] = part.get_content_type()
        content = part.get_payload(decode = False).decode('utf-8', 'ignore')
        json_part['content'] = clean_msg(content)
        json_msg['part'].append(json_part)
        
    # convert date from asctime to milliseconds since epoch using the $date descriptor, 
    # so it imports natively as ISODate object into MangoDB
    milli_date =  parse(json_msg['Date'])
    millis = int(time.mktime(milli_date.timetuple())*1000 + milli_date.microsecond/1000)
    json_msg['Date'] = {'$date': millis}
    
    return json_msg

# Generator, a function serves like an iterator
def gen_json_msgs(mb):
    while 1:
        msg = mb.next()
        if msg is None:
            break
        yield jsonifyMsg(msg)


def main():
    mbox_file = '[change to the location where you generate your .mbox output]'  # change to the location where you generate your .mbox output
    output_file = '[change to your output location]'  # change to your output location
    # remove enron.mbox.json before you re-run this code
    f = open(output_file, 'a')
    mb = mailbox.UnixMailbox(open(mbox_file, 'r'), email.message_from_file)
    for msg in gen_json_msgs(mb):
        if msg != None:
            f.write(json.dumps(msg, cls = Encoder) + '\n')
    
    f.close()
    
if __name__ == '__main__':
    main()
