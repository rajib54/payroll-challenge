# This class is used for json serialize payroll object

class Base:
    def toarray(self):
        data = {}
        for key, value in self.__dict__.items():
            data[key] = value
        return data