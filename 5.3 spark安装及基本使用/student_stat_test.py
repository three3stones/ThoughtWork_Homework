import unittest

import findspark
findspark.init()

from student_stat import student_grade_stat

class StudentStatTest(unittest.TestCase):
    def test_should_calculate_stat_of_student_data(self):
        stat = student_grade_stat('file:///C:/Users/10920/Desktop/student.csv')
        self.assertEquals(stat.well_count, 39)
        self.assertEquals(stat.less_well_count, 40)
        self.assertEquals(stat.not_good_count, 40)


if __name__ == '__main__':
    unittest.main()