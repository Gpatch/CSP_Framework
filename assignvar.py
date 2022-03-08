class AssignedVar:
    def __init__(self, var, value):
        self.var_name = var
        self.value = value

    def get_var_name(self):
        return self.var_name

    def get_var_value(self):
        return self.value

    def set_var_name(self, name):
        self.var_name = name

    def set_var_value(self, value):
        self.value = value
