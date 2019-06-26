'''
    Handles the url path for the entire app.
'''

from .urls_route.auth import AUTH_URL
from .urls_route.commerce import COMMERCE_URL
from .urls_route.store import STORE_URL
from .urls_route.feedback import CREATE_FEEDBACK
from .urls_route.lesson import LESSON_URL
from .urls_route.comments import COMMENT_URL
from .urls_route.analytics import ANALYTICS_URL
app_name = 'api'

urlpatterns = [
    *AUTH_URL,
    *ANALYTICS_URL,
    *COMMERCE_URL,
    *CREATE_FEEDBACK,
    *COMMENT_URL,
    *LESSON_URL,
    *STORE_URL,
]
