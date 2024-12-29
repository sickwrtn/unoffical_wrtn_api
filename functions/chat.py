from functions.variable import *
import requests
import json

class chat:
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