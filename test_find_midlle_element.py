from find_middle_element import *


class TestClass:
    def test_soma(self):
        assert gimme([2,3,1]) == 0
        assert gimme([3,2,1]) == 1
        assert gimme([1,3,2]) == 2
        assert gimme([10,100,1]) == 0
        assert gimme([223123,34,1]) == 1
        assert gimme([1,2,3]) == 1

