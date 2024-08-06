import hashlib
from django.core.cache import cache
'''
def generate_cache_key(view_name, *args, **kwargs):
    key = f"{view_name}:{':'.join(map(str, args))}:{':'.join(f'{k}={v}' for k, v in kwargs.items())}"
    return hashlib.md5(key.encode('utf-8')).hexdigest()

def get_cache_data(cache_key):
    return cache.get(cache_key)

def set_cache_data(cache_key, data, timeout=60*15):
    cache.set(cache_key, data, timeout)

'''

def generate_cache_key(prefix, *args, **kwargs):
    key = prefix
    for arg in args:
        key += f'_{arg}'
    for k, v in kwargs.items():
        key += f'_{k}_{v}'
    return key

def get_cache_data(cache_key):
    return cache.get(cache_key)

def set_cache_data(cache_key, data, timeout=3600):
    cache.set(cache_key, data, timeout)

def delete_cache_key(cache_key):
    cache.delete(cache_key)