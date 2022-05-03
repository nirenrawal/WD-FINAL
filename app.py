
from bottle import default_app, get, run, static_file



import Verification.GET.signup
import Verification.GET.login
import ROUTES.index_get
import ROUTES.admin
import Verification.POST.signup_post
import Verification.POST.login_post

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