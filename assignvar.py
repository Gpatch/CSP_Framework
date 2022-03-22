class AV:
    def __init__(self, name: str, value):
        self._name = name
        self._value = value

    def __str__(self):
        return f'{self._name} = {self._value}'

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val
