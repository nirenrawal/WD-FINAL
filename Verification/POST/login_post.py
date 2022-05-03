from bottle import post, request, redirect, response
import re
import g
import jwt
import uuid

@post("/login")
def login():
    if not request.forms.get("user_email"):
        response.status = 400
        return redirect("/login?error=user_email")

    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        return redirect("/login?error=user_email")

    user_email = request.forms.get("user_email")

    if not request.forms.get("user_password"):
        response.status = 400
        return redirect(f"/login?error=user_password&user_email={user_email}")

    if not re.match(g.REGEX_PASSWORD, request.forms.get("user_password")):
        response.status = 400
        return redirect("/login?error=user_password")

    # user_password = request.forms.get("user_password")

    for key in g.USERS:
        user_id = key
        if request.forms.get("user_email") == g.USERS[key]["user_email"]:
            if request.forms.get("user_password") == g.USERS[key]["user_password"]:
                encoded_user = jwt.encode({
                    "jwt_user_id": g.USERS[key]["user_id"],
                    "jwt_user_first_name": g.USERS[key]["user_first_name"], 
                    "jwt_user_last_name": g.USERS[key]["user_last_name"], 
                    "jwt_user_name": g.USERS[key]["user_name"], 
                    "jwt_user_image": g.USERS[key]["user_image"],
                    "session_id": str(uuid.uuid4())
                },
                    g.USER_SECRET, algorithm="HS256"
                )

                g.SESSIONS.append(encoded_user)

                response.set_cookie("jwt_user", encoded_user)

                response.status = 200
                return redirect(f"/tweet_user/{user_id}")
            else:
                response.status = 400
                return redirect(f"/login?error=user_password&user_email={user_email}")

    # if request.forms.get("user_email") == g.ADMIN[id]["admin_email"]:
    #         if request.forms.get("user_password") == g.ADMIN[id]["admin_password"]:

    #             encoded_admin = jwt.encode({
    #                 "admin_id": g.ADMIN["admin_id"],
    #                 "admin_user": g.ADMIN["admin_user"],
    #                 "session_id": str(uuid.uuid4())
    #             },
    #             g.ADMIN_SECRET, algorithm="HS256"
    #             )

    #             g.SESSIONS.append(encoded_admin)

    #             response.set_cookie("jwt_admin", encoded_admin)
    #             response.status = 200
    #             return redirect ("/admin")
    #         else:
    #             response.status = 400
    #             return redirect(f"/login?error=user_password&user_email={user_email}")

    return redirect("/login?error=user_email")



