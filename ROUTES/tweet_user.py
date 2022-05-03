from bottle import get, response, view, request, redirect
import g
import random
import jwt


############## User tweets / GET - ID ##############
@get('/tweet_user/<user_id>')
@view('tweet_user')
def _(user_id):

    try:
         # SESSSION
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in g.SESSION:
            return redirect("/login") 
        
        for session in g.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, g.USER_SECRET, algorithms=["HS256"])

        user_first_name=g.USERS[user_id]['user_first_name']
        user_last_name=g.USERS[user_id]['user_last_name']
        user_name=g.USERS[user_id]['user_name']
        user_image=g.USERS[user_id]['user_image']
        
        user_tweets = []
        if g.TWEETS == {}:
            return {'info': 'No tweets found yet!'}

        # get user_tweet by ID           
        for key in reversed(list(g.TWEETS.keys())): 
            if user_id in g.TWEETS[key]['user_id']:
                user_tweets.append(g.TWEETS[key])
        
        # random users
        users = []
        for key in g.USERS:
            users_dict = g.USERS
            users.append(users_dict[key])
            # random_users = [random.choice(list(users)) for i in range(4)]
       
        #response.content_type = 'application/json; charset=UTF-8'
        is_fetch = True if request.headers.get('From-Fetch') else False
        return dict(
                    is_fetch=is_fetch,
                    title="Tweet/User",

                    user_id=user_id,

                    user_tweets=user_tweets,

                    user_first_name=user_first_name,
                    user_last_name=user_last_name,
                    user_name=user_name,
                    user_image=user_image,

                    tabs=g.TABS, 
                    trends=g.TRENDS, 
                    items=g.ITEMS,

                    # random_users=random_users,
                    jwt_user=jwt_user
                    ) 
                

    except Exception as ex:
        print(ex)
        response.status = 500
        return "Something went wrong!!"