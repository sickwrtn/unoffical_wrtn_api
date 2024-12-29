[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=29&pause=1000&color=F7583A&center=true&width=435&lines=Unoffical+Wrtn+Api)](https://git.io/typing-svg)

## 사용방법
```py
from wrtn import wrtn

client = wrtn(token='<TOKEN>')
```

## 기능

### 유저정보조회
```py
client.user.nickname(client) #유저 name (string)
client.user.uid(client) #유저 uid (string)
client.user._id(client) #유저 id (string)
client.user.marketingAccountTerm(client) #계정생성일자 (string)
Client.user.isNewbie(client) #뉴비여부 (boolean)
```
----
