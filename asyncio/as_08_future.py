"""
Future 
Future are objectsthat the dont have any value right now, but in future they will have values


"""

import asyncio
from datetime import datetime

f = asyncio.Future()

# it doesnt have value, so it is not DONE
print(f.done())

# set a value for future instance
f.set_result("Alma")

# it does have a value, so the below print is True
print(f.done())
