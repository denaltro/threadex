from threadex import Thread


def func():
    return {'fizz': 'buzz'}


t = Thread(target=func)

t.start()
t.stop()

t.state  # ThreadStateEnum.STOPPED
t.result  # {'fizz': 'buzz'}, None
t.uptime  # smh > 0.0
