from wrtn import wrtn

client = wrtn(token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3NTg3NDQ3ODBkYzEwMWQxMzY4ODUxNyIsImVtYWlsIjoic2lsbG8xNTQyNjVAZ21haWwuY29tIiwid3J0blVpZCI6IjhGZGJCcmg3OGFZLUdHS09NMGROTnpoTCIsImlzc3VlciI6IndydG4iLCJpYXQiOjE3MzU0OTc0MzIsImV4cCI6MTczNTUwMTAzMn0.kKuql7T-uR6T-qYTVnioqNN4iFX76JBmbfM9ToV4tZQ')

print(client.chat.send_chat(client,message="안녕2",room_id="6771460d7f21ad8d290923bb0",isSuperMode=False))