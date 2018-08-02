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
    def test_bos(self):
        f = lambda x, y: x + y
        l = []
        t = ()
        r = range(0)
        s = ""
        with self.assertRaises(ValueError):
            reduce(f, l)
        with self.assertRaises(ValueError):
            reduce(f, t)
        with self.assertRaises(ValueError):
            reduce(f, r)
        with self.assertRaises(ValueError):
            reduce(f, s)

    def test_uclu(self):

        f = lambda x, y: x + y
        l = [1,2,3]
        t = (1,2,3)
        r = range(3)
        s = "abc"
        self.assertEqual(reduce(f, l), 6)
        self.assertEqual(reduce(f, t), 6)
        self.assertEqual(reduce(f, r), 3)
        self.assertEqual(reduce(f, s), "abc")
