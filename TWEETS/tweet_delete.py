from bottle import delete, response
import g
import re


##############  TWEETS/<ID> / DELETE  ################
@delete('/api-tweets/<tweet_id>')
def delete_tweet(tweet_id):
    try:
        if not re.match(g.REGEX_UUID4, tweet_id):
            response.status = 204
            return
        if tweet_id not in g.TWEETS:
            response.status = 204
            return
        
        g.TWEETS.pop(tweet_id)
        response.status = 200
        return {'info': "tweet deleted"}
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}