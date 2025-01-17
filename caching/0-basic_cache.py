#!/usr/bin/python3
"""  the bases of  dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ This class inherits from BaseCaching and is a caching system
        AND THE caching system doesn’t have limit """

    def put(self, key, item):
        """ Assigning the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value  """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
    
    
