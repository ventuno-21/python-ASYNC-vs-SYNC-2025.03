"""
Timer:
you can pause whatever operation you want for specific time
"""

from threading import Timer


def show():
    print(f"how you doing?")


t1 = Timer(5, show)
t1.start()
