class AssignedVar:
    def __init__(self, var, value, domain):
        self.var_name = var
        self.value = value
        self.domain = domain

    def __str__(self):
        return f'{self.var_name} = {self.value}'

    def get_var_name(self):
        return self.var_name

    def get_var_value(self):
        return self.value

    def get_var_domain(self):
        return self.domain

    def set_var_name(self, name):
        self.var_name = name

    def set_var_value(self, value):
        self.value = value

    def set_var_domain(self, domain):
        self.domain = domain
