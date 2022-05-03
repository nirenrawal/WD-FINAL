from datetime import datetime

NOW = datetime.now()
CREATED_DATE = NOW.strftime("%B %Y")
TWEET_UPDATED_AT = NOW.strftime('%b %d. %H:%M')


##############################################################
USER_SECRET ="dinamaraca"
ADMIN_SECRET = "COPENHAGEN"
##############################################################
SESSIONS = []
##############################################################
ADMIN = {
    "admin_id": "1",
    "admin_user": "admin",
    "admin_email": "admin@admin.com",
    "admin_password": "admin123"
}
##############################################################

USERS = {}
##############################################################

TWEETS = {}
##############################################################

REGEX_ID = "^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
##############################################################

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
##############################################################

REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
##############################################################

REGEX_USERNAME = '^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$'
##############################################################

REGEX_UUID4 = '^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
##############################################################

MIN_LEN = 1
MAX_LEN = 100


TABS = [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id": "home",  "href": "/home"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore",  "href": "/explore"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications",  "href": "/notifications"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages",  "href": "/messages"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks", "href": "/bookmarks"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists",  "href": "/lists"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile", "href": "/profile"},
    {"icon": "fa-solid fa-arrow-right-from-bracket", "title": "Logout", "id": "logout", "href": "/logout"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more",  "href": "/logout"}

]


TRENDS = [
    {"category": "Trending in Denmark", "title": "NFTs", "tweets_counter": "985K"},
    {"category": "Politics", "title": "Russia", "tweets_counter": "40k"},
    {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "50k"},
    {"category": "Music", "title": "Rock", "tweets_counter": "60k"},
    {"category": "News", "title": "Afganistan", "tweets_counter": "844k"},
]

ITEMS = [
    {"img": "barca.png", "title": "FC barcelona", "user_name": "FCBarcelona"},
    {"img": "bbc.png", "title": "BBC News world", "user_name": "BBCnewswrold"},
    {"img": "madrid.jpeg", "title": "RealMadrid", "user_name": "FCRealMadrid"},
]