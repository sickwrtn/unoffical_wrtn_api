[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=50&pause=1000&color=F7583A&center=true&height=400&width=600&lines=Unoffical+Wrtn+Api+1.1.4v)](https://git.io/typing-svg)
## wrtn 다운로드
```
pip install wrtn==1.1.4
```

## 사용방법
```py
from wrtn import Wrtn

client = Wrtn(refresh_token='<refresh_TOKEN>')
```
[예제](https://github.com/sickwrtn/unoffical_wrtn_api/tree/main/wrtn/exam) 한번 보고 사용해보는걸 추천

refresh Token찾는법은 크롬 개발자도구 열고 애플리케이션에 들어간 다음 cookies에 있는 refresh_token 을 가져오면 된다.

## 기능
모든함수에 있는 debug 매개변수(bool)는 오류있을때 true하고 뭐가문제인지 확인할때 쓰면 편함
### 유저정보조회
```py
client.user.nickname(self) #유저 name (string)
client.user.uid(self) #유저 uid (string)
client.user._id(self) #유저 id (string)
client.user.marketingAccountTerm(self) #계정생성일자 (string)
client.user.isNewbie(self) #뉴비여부 (bool)
```
### 채팅방기능
room_id는 채팅방조회 해보면 "_id": "\<id\>" 있을텐대 그거임 

아니면 본인 진행중인 채팅방 링크 보면 https://wrtn.ai/character/u/<캐릭터챗id>/c/<채팅방id> 이렇게 나올텐대 채팅방id 부분이다.
```py
client.chat.all_chat_list(self) #유저의 모든 챗방 조회
client.chat.chat_list(self,limit:int) #유저의 챗방을 limit개수만큼만 출력
client.chat.send(self,room_id:str,message:str,isSuperMode:bool=False) #해당room_id의 챗방에 메시지 보낸 후 답변 출력
client.chat.chat_log(self,room_id :str,limit:int) #해당room_id의 챗방에 있는 채팅내역을 limit개수 만큼 출력
```
### 피드조회
```py
client.feed.ranking(self,limit:int,period="daily") #일간랭킹을 limit개수만큼출력 period는 daily, monthly 있음 (순위순)
```
### 챗봇제작
```py
client.charmaker.make_char(self,data :dict) #챗봇 제작
client.charmaker.modify_char(self,data :dict,char_id :str) #챗봇 수정
```
### 챗봇 제작/수정을 위한 json form
제작
```py
{
            "name":"테스트4",
            "description":"테스트4",
            "profileImageUrl":"<이미지url>",
            "model":"sonnet",
            "initialMessages":["테스트4"],
            "characterDetails":"테스트4",
            "situationImages":[],
            "categoryIds":["65e809f21a9eea7b2f660937"],
            "tags":[],"visibility":"public",
            "promptTemplate":"simulation",
            "isCommentBlocked":false,
            "defaultStartingSetName":"기본 설정",
            "keywordBook":[
            {
                "keywords":["테스트"],
                "prompt":"테스트4",
                "name":"키워드 노트 1"
            }
            ],
            "isAdult":false
}
```
수정
```py
{
            "name":"테스트6",
            "description":"테스트5",
            "profileImageUrl":"<이미지url>",
            "model":"sonnet",
            "initialMessages":["테스트5"],
            "characterDetails":"테스트5",
            "replySuggestions":["안녕 테스트5! 어떻게 지내?","테스트5, 여기서 뭐하고 있었어? 뭔가 재밌는 일이 생겼어?","오, 테스트5! 요즘 어떤 일들이 있었는지 이야기 좀 해줘, 궁금해!"],
            "chatExamples":[],
            "situationImages":[],
            "categoryIds":["65e809f21a9eea7b2f660937"],
            "tags":[],
            "visibility":"public",
            "promptTemplate":"simulation",
            "isCommentBlocked":false,
            "defaultStartingSetName":"기본 설정",
            "startingSets":[],
            "keywordBook":[{
                "keywords":["테스트"],
                "prompt":"테스트5",
                "name":"키워드 노트 1"
            }
            ]
}
```
# 패치노트
## 1.1.4
```
wrtn.py refresh_token함수 예외처리
```
## 1.1.3
```
refresh token 기능 추가
wrtn.py 주석 추가
```
## 1.1.2
```
주석 추가
chat.send_chat -> chat.send 함수 이름변경
chat.send 예외처리
```
made by 뤼튼병자
