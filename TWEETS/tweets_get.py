from bottle import get, response, request
import g
import json
import re

##############  TWEETS / GET  #################### 
@get('/tweets')
def _():
    try:
        tweets = []
        if g.TWEETS == {}:
            response.status = 204
            return {'info': 'No tweets found yet!'}
        
        # tweets
        for key in reversed(list(g.TWEETS.keys())):
            tweets.append(g.TWEETS[key])
        
        

        response.status = 200
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweets=tweets))

        
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}


# ##############  TWEETS/<ID> / GET  ################
# @get('/tweets/<tweet_id>')
# def _(tweet_id):
#     try:
#         # Validate uuid
#         if not re.match(g.REGEX_UUID4, tweet_id):
#             response.status = 204
#             return
#         # Tweet not found
#         if tweet_id not in g.TWEETS:
#             response.status = 204
#             return
#         # Succes
#         tweet=g.TWEETS[tweet_id]

#         response.status = 200
#         response.content_type = 'application/json; charset=UTF-8'
#         return json.dumps(dict(tweet=tweet))
        
            
#     except Exception as ex:
#         print(ex)
#         response.status = 500
#         return {'info': 'Upps... something went wrong'}