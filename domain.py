class Domain:
    def __init__(self, var: str, domain: list):
        self._var = var
        self._domain = domain

    def __str__(self):
        return f'{self._var} @ {self._domain}'

    @property
    def var(self):
        return self._var

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, dom):
        self._domain = dom

    def domain_add(self, val):
        exists = False
        for d in self._domain:
            if d == val:
                exists = True
                break
        if not exists:
            self._domain.append(val)

    def domain_del(self, val):
        self._domain.remove(val)


