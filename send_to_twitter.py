import twitter

CONSUMER_KEY = 's8Rs4pS31m4u5jyYpPaiF7xsm' # Same as API key
CONSUMER_SECRET = 'JPe4yTPU1PELCIuVFdofXswuCppFJC8Gfyny6TbiaGFjjLbJ6H' # Same as API secret
ACCESS_TOKEN_KEY= '1118868396-Cn1MRYZeKRZxp519RAHjJpc8DLk9Z2cNzhHbqDk'
ACCESS_TOKEN_SECRET= 'yiiiOzNTEPS3WdNohDoAE0k8V0IFpENtqLByhon0BWApK'

'''
Post a tweet to my Twitter account
'''
def send_to_twitter():
    msg = "I am a message that will be sent to Twitter"
    if len(msg) > 140:
        raise Exception ('Message too long!')
    else:
        authkey = twitter.Twitter(auth=twitter.OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
        result = authkey.statuses.update(status=msg)
        return result

send_to_twitter()
