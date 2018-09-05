from random import randint
class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):
    a = set()
    for _ in range(10):
        a.add(randint(0, 100))

    @staticmethod
    def get_array():
        # complete this function
        a = TestDataUniqueValues.a
        return list(a)

    @staticmethod
    def get_expected_result():
        # complete this function
        a = TestDataUniqueValues.get_array()
        return a.index(min(a))

class TestDataExactlyTwoDifferentMinimums(object):
    a = set()
    for _ in range(10):
        a.add(randint(0, 100))
    a = list(a)
    a.append(min(a))

    @staticmethod
    def get_array():
        # complete this function
         a =  TestDataExactlyTwoDifferentMinimums.a
         return a

    @staticmethod
    def get_expected_result():
        # complete this function
        a = TestDataExactlyTwoDifferentMinimums.get_array()
        return a.index(min(a))