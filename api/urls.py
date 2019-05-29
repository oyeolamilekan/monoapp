'''
    Handles the url path for the entire app.
'''

from .urls_route.auth import AUTH_URL
from .urls_route.commerce import COMMERCE_URL
from .urls_route.store import STORE_URL
from .urls_route.feedback import CREATE_FEEDBACK
app_name = 'api'

urlpatterns = [
    *AUTH_URL,
    *COMMERCE_URL,
    *STORE_URL,
    *CREATE_FEEDBACK
]
