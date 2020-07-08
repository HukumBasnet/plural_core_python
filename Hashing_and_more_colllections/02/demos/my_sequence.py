from collections.abc import MutableSequence

class ModTwoSequence(MutableSequence):
    _list:list = []

    def __repr__(self):
        return self._list.__repr__()
    
    def _validate(self, value):
        if value % 2 != 0:
            raise ValueError

    def insert(self, index, value):
        self._validate(value)
        self._list.insert(index, value)

    def __delitem__(self, index):
        del self._list[index]

    def __setitem__(self, index, value):
        self._validate(value)
        self._list[index] = value

    def __getitem__(self, index):
        return self._list[index]
    
    def __len__(self):
        return len(self._list)