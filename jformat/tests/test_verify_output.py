import os

class TestLongComparisons():

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup(self):
        self.first = "this is one very long string"

    def teardown(self):
        pass

    def utility(self, contents=''):
        # create the file
        pass

    def test_compare_large_strings(self):
        self.utility()
        second = "this is one very long string"
        assert self.first == second

    def test_basic(self):
        assert True

    def test_compare_large_lists_to_none(self):
        #first = ["this", "is", "one", "very", "long", "list"]
        first = self.first.split()
        second = ["this", "is", "one", "very", "long", "list"]
        assert first != None
