from mailcatcher import Mailcatcher

mc = Mailcatcher('localhost', 1080)

# Subscrive Mailcatcher
mc.observable() \
    .subscribe(lambda msg: print(msg.subject))
