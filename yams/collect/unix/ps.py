from yams.collect import BaseCollector

import psutil


class ProcessCollector(BaseCollector):

    def disk_usage(self, property_name, path):
        def _f(property_name, path):
            self.write(
                property_name, psutil.disk_usage(path).percent)
        self.schedule(_f, property_name, path)

    def cpu_usage(self, property_name):
        def _f(property_name):
            self.write(
                property_name, psutil.cpu_percent(interval=0)
            )
        self.schedule(_f, property_name)

    def count_process(self, property_name, query):
        def _f(property_name, query):
            result = 0
            for p in psutil.process_iter():
                if (
                    query in p.name() or
                    query in ' '.join(p.cmdline())
                ):
                    result = result + 1
            self.write(property_name, result)
        self.schedule(_f, property_name, query)