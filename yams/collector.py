import sys
from yams.collect import unix, win
from yams import select_collector

if 'linux' in sys.platform:
    select_collector.install(unix)
else:
    select_collector.install(win)