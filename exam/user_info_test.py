from wrtn import wrtn

client = wrtn(token='<TOKEN>')

print(client.user.nickname(client))
print(client.user.uid(client))
