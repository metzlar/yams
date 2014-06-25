import memcache


mc = memcache.Client(['127.0.0.1:11211'], debug=0)


def set(key, value):
    return mc.set(key, value)

def get(key):
    return mc.get(key)