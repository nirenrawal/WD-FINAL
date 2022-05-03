import os
from bottle import post, request, redirect, response
import re
import uuid
import g
import json
import imghdr

@post("/signup")
def signup():
    # REGEX VALIDATION
    if not re.match(g.REGEX_USERNAME, request.forms.get("user_name")):
        response.status = 400
        return "Username must contain 5 to 20 characters or numbers and only '.', '-' and '_' characters are allowed "

    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        return "Please insert a valid email"

    if not re.match(g.REGEX_PASSWORD, request.forms.get("user_password")):
        response.status = 400
        return "Password must contain minimum eight characters, at least one letter and one number"
    
    user_id = str(uuid.uuid4())
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_email = request.forms.get("user_email")
    user_name = request.forms.get("user_name")
    user_password = request.forms.get("user_password")

    for key in g.USERS:
        if g.USERS[key]["user_email"] == request.forms.get("user_email"):
            return redirect("/signup?error=email_exists&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")

    
    image = request.files.get("user_image")
    if not image:
        g.USERS[user_id] = {
            "user_id": user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_name": user_name,
            "user_email": user_email, 
            "user_password":user_password,
            "user_image": "",
            "user_signup_date": g.CREATED_DATE
        }
    else:
        file_name, file_extension = os.path.splitext(image.filename)
        print(file_name)
        print(file_extension)

        if file_extension not in ('.png', '.jpeg', '.jpg'):
            return 'Image not allowed!'

        if file_extension == ".jpg": file_extension = ".jpeg"

        image_id = str(uuid.uuid4())
        image_name = f"{image_id}{file_extension}"
        image_path = f"./images/user_image{image_name}"
        json.dumps(str(image_name))

        imghdr_extension = imghdr.what(image_path)

        if file_extension != f".{imghdr_extension}":
            os.remove(image_path)
            response.status = 400
            return "Invalid image format!!"



        g.USERS[user_id] = {
             "user_id": user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_name": user_name,
            "user_email": user_email, 
            "user_password":user_password,
            "user_image": image_name,
            "user_signup_date": g.CREATED_DATE,
            "user_cover_image": ""
        }

    response.status = 200
    return redirect("/login")