import time
import os, sys


class BaseCollector(list):

    def __init__(
        self, path = '/tmp/yams', limit_execution_seconds = 0
    ):
        self.path = path
        self.start = time.time()
        self.limit_execution_seconds = limit_execution_seconds

        if not os.path.exists(self.path):
            os.makedirs(self.path)
        

    def schedule(self, func, *args, **kwargs):
        self.append((func, args, kwargs))
        
    def write(self, name, result):
        with open(os.path.join(self.path, name), 'w+') as f:
            f.write(unicode(result))

    def run(self):
        while(True):
            for (func, args, kwargs) in self:
                func(*args, **kwargs)

                if (
                    self.limit_execution_seconds > 0 and
                    (
                        time.time() - self.start
                    ) > self.limit_execution_seconds
                ):
                    sys.exit()
                
                time.sleep(0.5)


class MultiCollector(BaseCollector):
    def schedule(self, *args, **kwargs):
        raise Exception((
            'Do not schedule using this collector! '
            'Append collectors from yams.collector to this '
            'collector instead.'
        ))
    
    def run(self):
        while(True):
            for collector in self:
                for (func, args, kwargs) in collector:
                    func(*args, **kwargs)

                    if (
                        self.limit_execution_seconds > 0 and
                        (
                            time.time() - self.start
                        ) > self.limit_execution_seconds
                    ):
                        sys.exit()
                
                    time.sleep(0.5)
