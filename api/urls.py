'''
    Handles the url path for the entire app.
'''

from api.urls_route.analytics import ANALYTICS_URL
from api.urls_route.auth import AUTH_URL
from api.urls_route.comments import COMMENT_URL
from api.urls_route.commerce import COMMERCE_URL
from api.urls_route.feedback import CREATE_FEEDBACK
from api.urls_route.lesson import LESSON_URL
from api.urls_route.store import STORE_URL
from api.urls_route.allies import ALLIES_URL
app_name = 'api'

urlpatterns = [
    *AUTH_URL,
    *ANALYTICS_URL,
    *COMMERCE_URL,
    *CREATE_FEEDBACK,
    *COMMENT_URL,
    *LESSON_URL,
    *STORE_URL,
    *ALLIES_URL
]
