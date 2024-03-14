"""定义请求 url."""

from .config import server

urls = {
    "home":'',
    "login":'login/',
    "logout":'logout/',
    "dashboard":'dashboard/',
    "draft":'draft/',
    "text":'text/',
    "picture":'picture/',
    "pictures":'pictures/',
    "audio":'audio/',
    "audios":'audios/',
}




def getUrl(key:str):
    """获取 url."""
    return server + urls[key]
