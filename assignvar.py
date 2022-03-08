class AssignedVar:
    def __init__(self, var, value):
        self.var = var
        self.value = value

    def get_var_name(self):
        return self.var

    def get_var_value(self):
        return self.value
