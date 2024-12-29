from functions.variable import *
import requests
import json

class user:
    def direct_info(self):
        res = requests.put(f"{url}/be/user", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)
    def nickname(self):
        res = requests.put(f"{url}/be/user", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)['data']['name']
    def uid(self):
        res = requests.put(f"{url}/be/user", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)['data']['wrtnUid']
    def _id(self):
        res = requests.put(f"{url}/be/user", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)['data']['_id']
    def marketingAccountTerm(self):
        res = requests.put(f"{url}/be/user", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)['data']['marketingTerm']
    def isNewbie(self):
        res = requests.put(f"{url}/be/user", headers=self.cookie)
        if res.status_code != 200:
            raise Exception(res.status_code)
        return json.loads(res.text)['data']['isNewbie']
