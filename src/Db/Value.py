class DbValue:

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class DateValue(DbValue):
    pass


class ClobValue(DbValue):
    pass


class BlobValue(DbValue):
    pass


class LiteralValue(DbValue):
    pass


class SequenceValue(DbValue):
    pass
