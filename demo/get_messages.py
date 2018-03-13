from mailcatcher import Mailcatcher

mc = Mailcatcher('localhost', 1080)

# Get All Messages
msgs = mc.messages()

for msg in msgs:
    print(msg.subject)
