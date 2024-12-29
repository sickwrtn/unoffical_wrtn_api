class wrtn:
    from functions.user import user as user
    from functions.chat import chat
    from functions.feed import feed
    def __init__(self,token:str):
        self.cookie = {f"Authorization": f"Bearer {token}"}