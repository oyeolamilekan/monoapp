import requests
import json

def get_location(user_ip):
    """[Returns a detailed info about the user]
    
    Arguments:
        user_ip {[ string ]} -- [it gets user ip and gets needed info]
    
    Returns:
        [type] -- [description]
    """
    get_user_info = requests.get(
        "http://api.ipstack.com/{}?access_key=e0938a30e3c9b870654ba09fcd8da19e".format(
            user_ip
        )
    ).json()
    return get_user_info
