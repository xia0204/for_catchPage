import gevent
from gevent import monkey,Greenlet
import requests
import time
import multiprocessing

# def test0():
#     # g2.switch()
#     print(1)
#
#
#
# def test1():
#     time.sleep(2)
#     print('test1')
#     g1.switch()
#     # print(3)
#     # # gevent.sleep(0)
#     # print(4)
#
# g1 = Greenlet(test1)
# g2 = Greenlet(test0)
# g1.switch()
def foo(message, n):
    """
    Each thread will be passed the message, and n arguments
    in its initialization.
    """
    gevent.sleep(n)
    print(message)


# Initialize a new Greenlet instance running the named function
# foo
thread1 = Greenlet.spawn(foo, "Hello", 1)

# Wrapper for creating and running a new Greenlet from the named
# function foo, with the passed arguments
thread2 = gevent.spawn(foo, "I live!", 2)

# Lambda expressions
thread3 = gevent.spawn(lambda x: (x + 1), 2)

threads = [thread1, thread2, thread3]

# Block until all threads complete.


gevent.joinall(threads)



















