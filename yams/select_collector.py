import sys
import yams

def install(collector):
    yams.collector = collector
    sys.modules['yams.collector'] = collector