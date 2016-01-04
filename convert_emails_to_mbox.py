'''
Created on Dec 31, 2015
@author: hanhanwu
Convert Enron corpus to standardized mbox format
'''
import os
import re
from time import asctime
import email
from dateutil.parser import parse


def main():
    folder_path = '[change to you enron email dataset location]'  # change to you enron email dataset location
    # remove enron.mbox before you re-run this code
    output_path = '[change to your output path]'  # change to your output path
    mbox = open(output_path, 'a')
    for (root, dirs, file_names) in os.walk(folder_path):
        if root.split(os.sep)[-1] != 'inbox':
            continue
        
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            message_text = open(file_path).read()
            
            msg_from = re.search(r"From: ([^\r]+)", message_text).group(1)
            msg_date = re.search(r"Date: ([^\r]+)", message_text).group(1)
            msg_date = asctime(parse(msg_date).timetuple())
            print msg_from, msg_date
            
            msg = email.message_from_string(message_text)
            msg.set_unixfrom('From %s %s' % (msg_from, msg_date))
            
            mbox.write(msg.as_string(unixfrom=True) + '\n\n')
            
    mbox.close()
    
if __name__ == '__main__':
    main()

