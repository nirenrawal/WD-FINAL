from bottle import get, response, view, request, redirect
import g



@get("/admin")
@view("admin")
def admin():
    try:
       
        user_jwt = request.get_cookie("jwt_admin")
        if user_jwt not in g.SESSION:
            return redirect("/login") 

        tweets = []
        if g.TWEETS == {}:
            return "No tweets found"
        
   
        for key in reversed(list(g.TWEETS.keys())):
            tweets.append(g.TWEETS[key])

        return dict(tweets=tweets)

    except Exception as ex:
        print(ex)
        response.status = 500
        return "Something went wrong!!"
