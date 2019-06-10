import sys
import time
import itertools

try:
    xrange  # @UndefinedVariable
except NameError:
    xrange = range
    
from itertools import groupby
count = itertools.count(0)
def next_val():
    return next(count) % 25

if '--simple-trace' in sys.argv or True:

    def trace_dispatch(frame, event, arg):
        return trace_dispatch

    sys.settrace(trace_dispatch)

start_time = time.time()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# create an array of random strings of 40 characters each
l = sorted([''.join([letters[next_val()] for _ in range(40)]) for _ in xrange(10000)])
# group by the first two characters
g = {k: list(v) for k, v in groupby(l, lambda x: x[:2])}


if False:
    pass  # Breakpoint here

print('TotalTime>>%s<<' % (time.time()-start_time,))
print('TEST SUCEEDED')