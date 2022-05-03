from bottle import post, response, request
import json
import g
import uuid
from datetime import datetime
import os
import imghdr
import re

@post('/tweets/<user_id>')
def _(user_id):

    try:
        tweet_id = str(uuid.uuid4())
        if not re.match(g.REGEX_UUID4, tweet_id):
            response.status = 204
            return

        if not request.forms.get('tweet_text'):
            response.status = 400
            return "Something is wrong"
        
        tweet_text = request.forms.get('tweet_text').strip()
        
        if len(tweet_text) < g.MIN_LEN:
            response.status = 400
            return f"tweet description must be minimun {g.MIN_LEN}"

        if len(tweet_text) > g.MAX_LEN:
            response.status = 400
            return f"tweet description must be maximum {g.MAX_LEN}"

       # upload
        ##################################################  IMAGE  ######################################################
        # Upload image
        image = request.files.get('tweet_image')

        # tweet without image
        if not image:
            g.TWEETS[tweet_id] = {
                    "tweet_id": tweet_id,
                    'user_id': user_id,
                    'user_first_name': g.USERS[user_id]['user_first_name'],
                    'user_last_name': g.USERS[user_id]['user_last_name'],
                    'user_name': g.USERS[user_id]['user_name'],
                    'user_image': g.USERS[user_id]['user_image'],
                    'tweet_text': tweet_text,
                    'tweet_created_at': g.CREATED_DATE
                    }
        else:
            file_name, file_extension = os.path.splitext(image.filename)
            # print(file_name)
            # print(file_extension)

            if file_extension not in ('.png', '.jpeg', '.jpg'):
                return 'Image not allowed!'

            if file_extension == ".jpg": file_extension = ".jpeg"

            image_id = str(uuid.uuid4())
            image_name = f'{image_id}{file_extension}'

            # Save the image
            image_path = f'./images/{image_name}'
            image.save(image_path)

            json.dumps(str(image_name))

            print("imghdr.what", imghdr.what(image_path))  
            print("file_extension", file_extension)                
            imghdr_extension = imghdr.what(image_path)
            
            if file_extension != f".{imghdr_extension}":
                print("mmm... suspicious ... it is not really an image")
                os.remove(image_path)
                return "mmm... got you! It was not an image"

            

            # tweet with image
            if user_id in g.USERS:
                g.TWEETS[tweet_id] = {
                    "tweet_id": tweet_id,
                    'user_id': user_id,
                    'user_first_name': g.USERS[user_id]['user_first_name'],
                    'user_last_name': g.USERS[user_id]['user_last_name'],
                    'user_name': g.USERS[user_id]['user_name'],
                    'user_image': g.USERS[user_id]['user_image'],
                    'tweet_text': tweet_text,
                    'tweet_image': image_name,
                    'tweet_created_at': g.CREATED_DATE
                    }
                response.status = 201
                
            else:
                return "User Id doesn't match"        
        
    except Exception as ex:
        print(ex)
        response.status = 500
        return "Oops something went wrong!!"

    return json.dumps(dict(tweet=g.TWEETS[tweet_id]))