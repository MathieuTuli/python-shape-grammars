__author__ = 'root-11'


class Database(object):
    """ author: root-11
    A dictionary that allows multiple keys for one value
    """

    def __init__(self):
        '''author: root-11
        '''
        self.keys = {}
        self.values = {}

    def __contains__(self, item):
        '''author: Mathieu Tuli
        '''
        return item in self.keys

    def __getitem__(self, item):  # <---SQL SELECT statement
        '''author: root-11
        '''
        values = self.keys[item]
        if len(values) > 1:
            return sorted(list(values))
        elif len(values) == 1:
            return list(values)[0]

    def __setitem__(self, key, value):
        '''author: root-11
        '''
        if key not in self.keys:  # it's a new key <---SQL INSERT statement
            if value not in self.values:  # it's a new value
                self.keys[key] = set()  # a new set
                self.keys[key].add(value)
                self.values[value] = set()  # a new set
                self.values[value].add(key)
            elif value in self.values:
                self.keys[key] = set()  # a new set
                self.keys[key].add(value)  # a new key
                self.values[value].add(key)  # but just an update to the values
        elif key in self.keys:  # it's a new relationships
            self.keys[key].add(value)
            if value not in self.values:
                self.values[value] = set()
                self.values[value].add(key)
            elif value in self.values:
                self.values[value].add(key)

    def update(self, key, old_value, new_value):
        """author: root-11
        update is a special case because __setitem__ can't see that
        you want to propagate your update onto multiple values. """
        if old_value in self.keys[key]:
            affected_keys = self.values[old_value]
            for key in affected_keys:
                self.__setitem__(key, new_value)
                self.keys[key].remove(old_value)
            del self.values[old_value]
        else:
            raise KeyError(
                "key: {} does not have value: {}".format(key, old_value))

    def __delitem__(self, key, value=None):  # <---SQL DELETE statement
        '''author: root-11
        '''
        if value is None:
            # All the keys relations are to be deleted.
            try:
                value_set = self.keys[key]
                for value in value_set:
                    self.values[value].remove(key)
                    if not self.values[value]:
                        del self.values[value]
                del self.keys[key]  # then we delete the key.
            except KeyError:
                raise KeyError("key not found")
        else:  # then only a single relationships is being removed.
            try:
                if value in self.keys[key]:  # this is a set.
                    self.keys[key].remove(value)
                    self.values[value].remove(key)
                # if the set is empty, we remove the key
                if not self.keys[key]:
                    del self.keys[key]
                # if the set is empty, we remove the value
                if not self.values[value]:
                    del self.values[value]
            except KeyError:
                raise KeyError("key not found")

    def iterload(self, key_list, value_list):
        '''author: root-11
        '''
        for key in key_list:
            for value in value_list:
                self.__setitem__(key, value)
