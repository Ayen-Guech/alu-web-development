#!/usr/bin/python3
"""The LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This  Class inherits from BaseCaching ,the caching system """

    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ Assigning to the dictionary, LIFO algorithm that add element """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """ Returning the value what is linked """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
