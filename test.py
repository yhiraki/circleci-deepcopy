import copy
import unittest

data = {
    'hoge': 1,
    'fuga': {
        'piyo': 2
    }
}


class Test(unittest.TestCase):

    def setUp(self):
        self.d = copy.deepcopy(data)

    def test_a(self):
        with self.assertRaises(KeyError):
            self.d['fuga']['moge']
        self.assertEqual(self.d['fuga']['piyo'], 2)
        self.d['fuga']['moge'] = 1
        self.assertEqual(self.d['fuga']['moge'], 1)

    def test_b(self):
        with self.assertRaises(KeyError):
            self.d['fuga']['moge']
        self.assertEqual(self.d['fuga']['piyo'], 2)
        self.d['fuga']['moge'] = 1
        self.assertEqual(self.d['fuga']['moge'], 1)

    def test_c(self):
        with self.assertRaises(KeyError):
            self.d['fuga']['moge']
        self.assertEqual(self.d['fuga']['piyo'], 2)
        self.d['fuga']['moge'] = 1
        self.assertEqual(self.d['fuga']['moge'], 1)


if __name__ == '__main__':
    unittest.main()
