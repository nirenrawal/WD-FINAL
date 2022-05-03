from bottle import get, request, response, view
import g
import json

@get("/signup")
@view("signup")
def signup():
    try:
        error = request.params.get("error")
        user_first_name = request.params.get("user_first_name")
        user_last_name = request.params.get("user_last_name")
        user_email = request.params.get("user_email")
        user_name = request.params.get("user_name")
        email_already_exists = request.params.get("email_already_exists")
        user_password = request.params.get("user_password")

       

        is_fetch = True if request.headers.get('From-Fetch') else False
        page_title = "signup"
        return dict(
            title=page_title,
            is_fetch=is_fetch,

            error =error,
            user_first_name=user_first_name,
            user_last_name = user_last_name,
            user_email = user_email,
            user_name = user_name,
            email_already_exists = email_already_exists,
            user_password = user_password
            
            )
     

    except Exception as ex:
        print(ex)
        response.status = 500
        return "something went wrong please try again!!!"