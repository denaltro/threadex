# Threadex

Threadex is a small package that will allow manipulate python threads: start, stop and get some data/stats.

## Build

```
python setup.py sdist
pip install ../dist/threadex-0.0.1.tar.gz
```

## Usage

```
from threadex import Thread

def func():
    return {'fizz': 'buzz'}

t = Thread(target=func)

t.start() # to start thread
t.stop() # to stop thread

t.state  # get current thread state
t.result  # get result of target function
t.uptime  # get uptime in monotonic time
```