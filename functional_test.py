# -*- coding: utf-8 -*-

import unittest
import functional

class TestFunctional(unittest.TestCase):

    def test_sum(self):
        r1 = 1 + 2 + 3 + 4 - 5
        r2 = functional.sum(1, 2, 3, 4, -5)
        self.assertEqual(r1, r2)

    def test_mul(self):
        r1 = 1 * 2 * 3 * 4 * -5
        r2 = functional.mul(1, 2, 3, 4, -5)
        self.assertEqual(r1, r2)

    def test_coalesce(self):
        r1 = functional.coalesce(None, '', 0, 1.0)
        self.assertEqual(r1, '')
        r2 = functional.coalesce(None, None, None)
        self.assertIsNone(r2)
    
    def test_noneif(self):
        r1 = functional.noneif('', 0)
        self.assertEqual(r1, '')
        r2 = functional.noneif(0.0, 0)
        self.assertIsNone(r2)

if __name__ == '__main__':
    unittest.main()