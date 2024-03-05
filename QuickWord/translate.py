import requests
import hashlib
from config import appid, secret_key

class BaiduTranslator:
    def __init__(self, appid, secret_key):
        self.appid = appid
        self.secret_key = secret_key
        self.base_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"

    def translate_text(self, text, from_lang="en", to_lang="zh"):
        salt = "1435660288"
        sign = hashlib.md5((self.appid + text + salt + self.secret_key).encode()).hexdigest()
        params = {
            "q": text,
            "from": from_lang,
            "to": to_lang,
            "appid": self.appid,
            "salt": salt,
            "sign": sign
        }

        response = requests.get(self.base_url, params=params)
        result = response.json()

        if "trans_result" in result:
            translation = result["trans_result"][0]["dst"]
            return translation
        else:
            return None

translator = BaiduTranslator(appid, secret_key)

