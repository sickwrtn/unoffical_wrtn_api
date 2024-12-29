from wrtn import wrtn

client = wrtn(token='<TOKEN>')

print(client.chat.all_chat_list(client))
print(client.chat.send_chat(client,message="안녕",room_id="<채팅방id>",isSuperMode=False))

