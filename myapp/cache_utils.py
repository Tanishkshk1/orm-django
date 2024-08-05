import hashlib
from django.core.cache import cache

def generate_cache_key(view_name, *args, **kwargs):
    key = f"{view_name}:{':'.join(map(str, args))}:{':'.join(f'{k}={v}' for k, v in kwargs.items())}"
    return hashlib.md5(key.encode('utf-8')).hexdigest()

def get_cache_data(cache_key):
    return cache.get(cache_key)

def set_cache_data(cache_key, data, timeout=60*15):
    cache.set(cache_key, data, timeout)
