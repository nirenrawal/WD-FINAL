from bottle import get, request, response, view
import g



##############  USERS / GET  #################### 
@get('/users-tweets/<tweet_id>')
def tweets(tweet_id):

    try:
        return dict(tweets=g.TWEETS[tweet_id])
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}

##############  USERS/you may like / GET  #################### 
# @get('/api-users-you-might-like')

# def _():

#     try:
#         # users = []
#         # for key in data.USERS:
#         #     userx = data.USERS
#         #     users.append(userx[key])
#         #     random_users = [random.choice(list(users)) for i in range(4)]

#         for key in data.USERS:
#             keys = random.sample(list(data.USERS), 3)

#         return dict(random_users=keys)   

#     except Exception as ex:
#         print(ex)
#         response.status = 500
#         return {'info': 'Upps... something went wrong'}
