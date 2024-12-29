import requests
import json

url = "https://api.wrtn.ai"
url2 = "https://api2.wrtn.ai"
class wrtn_api:
    def __init__(self,token:str):
        self.cookie = {f"Authorization": f"Bearer {token}"}
        print(self.cookie)
    #유저 정보 가져오기
    def user_info(self):
        res = requests.put(f"{url}/be/user", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)
    def all_chat_list(self):
        res = requests.get(f"{url}/be/api/v2/chat", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)
    def chat_list(self,limit:int):
        res = requests.get(f"{url}/be/api/v2/chat?type=character&limit={limit}", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)
    def send_chat(self,_id:str,message:str,isSuperMode:bool=False):
        data = {"message":message,"reroll":False,"images":[],"isSuperMode":isSuperMode}
        res_send = requests.post(f"{url2}/terry/characters/chat/{_id}/message",headers=self.cookie,json=data)
        if res_send.status_code != 201:
            raise Exception(res_send.status_code)
        json_res = json.loads(res_send.text)
        res_recieve = requests.get(f"{url2}/terry/characters/chat/{_id}/message/{json_res["data"]}",headers=self.cookie)
        return res_recieve.text
    def ranking(self,limit:int,period="daily"):
        res = requests.get(f"{url}/be/characters/ranking?limit={limit}&period={period}", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)
