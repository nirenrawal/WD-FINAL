from bottle import get, request, response, view

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