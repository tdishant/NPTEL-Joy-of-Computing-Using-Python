from datetime import datetime as dt
import pytz
#current time
print(dt.now())
print(dt.today())
#current time at singapore 
tz = pytz.timezone('Singapore')
print(dt.now(tz))