"""
    Event : event is mechanisim for communication between threads
    
"""

from threading import Event, Thread


def first(f, s):
    print("1st is ready")
    f.set()
    s.wait()
    print("1st is working")
    f.clear()


def second(f, s):
    print("2nd is ready")
    s.set()
    f.wait()
    print("2nd is working")
    s.clear()


f = Event()
s = Event()


t1 = Thread(target=first, args=(f, s))
t2 = Thread(target=second, args=(f, s))

t1.start()
t2.start()
