
from bottle import default_app, get, request, response, run, static_file, view
import Verification.GET.signup
import Verification.GET.login
import Verification.POST.signup_post


@get("/")
@view("index.html")
def index():
    try:
        is_fetch = True if request.headers.get("From-Fetch") else False
        return dict(title="My Twitter", is_fetch=is_fetch)
    except Exception as ex:
        print(ex)
        response.staus = 500
        return "Something is wrong!!"

#############################################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

#############################################
@get("/images/<image_name>")
def _(image_name):
    return static_file(image_name, root="./images")
#############################################
@get("/app.js")
def _():
    return static_file("app.js", root=".")

#############################################
@get("/validator.js")
def _():
    return static_file("validator.js", root=".")

#############################################



try:
    import production
    application = default_app()
except:
    run(host='127.0.0.1', port=5555, debug=True, reloader=True, server="paste")