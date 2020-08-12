import unittest

from rect import Rect


class RectTest(unittest.TestCase):
    # 矩阵A包含矩阵B
    def test_intersect_for_crossing_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1, 1, 0.5, 0.5)))

    # 矩阵A和矩阵B相交
    def test_intersect_for_crossing_rects_0(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1.5, 1.5, 2, 2))) 
    
    # 矩阵A的右上点与矩阵B的左下点重合
    def test_intersect_for_crossing_rects_1(self):
        self.assertFalse(Rect(1, 1, 1, 1).intersect(Rect(2, 2, 2, 2)))

    # 矩阵A和矩阵B不相交
    def test_intersect_for_crossing_rects_2(self):
        self.assertFalse(Rect(1, 1, 1, 1).intersect(Rect(3, 3, 2, 2)))


if __name__ == '__main__':
    unittest.main()