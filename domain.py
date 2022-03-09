class Domain:
    def __init__(self, domain):
        self.domain = domain

    def __str__(self):
        return f'@{self.domain}'

    def add_to_domain(self, val):
        exists = False
        for i in self.domain:
            if i == val:
                exists = True
                break
        if not exists:
            self.domain.append(val)

    def del_from_domain(self, val):
        for i in self.domain:
            if i == val:
                self.domain.remove(val)
                break


