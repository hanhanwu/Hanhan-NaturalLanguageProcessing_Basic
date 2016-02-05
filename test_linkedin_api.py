'''
Created on Jan 24, 2016
@author: hanhanwu
Linkedin token has very short life span
Check this url for getting your token:
https://developer.linkedin.com/docs/oauth2
'''


from linkedin import linkedin as lk

new_token = '[your token]'  # change this to your token

application = lk.LinkedInApplication(token=new_token)

p = application.get_profile()
c = application.get_connections()   # this one no longer works
print p
print c
