import hashlib
from django.core.cache import cache

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