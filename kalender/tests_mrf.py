import unittest
from mrf import map, reduce, filter


class MapTests(unittest.TestCase):
    def test_bos(self):
        f = lambda x: x + 1
        l = []
        t = ()
        r = range(0)
        s = ""
        self.assertListEqual(map(f, l), [])
        self.assertListEqual(map(f, t), [])
        self.assertListEqual(map(f, r), [])
        self.assertListEqual(map(f, s), [])

    def test_dolu(self):
        f = lambda x: x + 1
        g = lambda x: x + "1"
        l = [1]
        t = (1,)
        r = range(1)
        s = "a"
        self.assertListEqual(map(f, l), [2])
        self.assertListEqual(map(f, t), [2])
        self.assertListEqual(map(f, r), [1])
        with self.assertRaises(TypeError):
            map(f, s)
        self.assertListEqual(map(g, s), ["a1"])

    def test_coklu(self):
        f = lambda x: x + 1
        g = lambda x: x + "1"
        l = [1, 2]
        t = (1, 2)
        r = range(2)
        s = "ab"
        self.assertListEqual(map(f, l), [2, 3])
        self.assertListEqual(map(f, t), [2, 3])
        self.assertListEqual(map(f, r), [1, 2])
        with self.assertRaises(TypeError):
            map(f, s)
        self.assertListEqual(map(g, s), ["a1", "b1"])


class FilterTests(unittest.TestCase):
    pass


class ReduceTests(unittest.TestCase):
    pass
