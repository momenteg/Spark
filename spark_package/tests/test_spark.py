import unittest
from spark_application.util.spark import init_spark
import databricks.koalas as ks


class TestSpark(unittest.TestCase):
    def setUp(self):
        self.dataset = [("abc", 1), ("def", 2)]
        self.columns = ["name", "age"]
        self.df = ks.DataFrame(data=self.dataset, columns=self.columns)

    def test_len_df(self):
        self.assertEqual(len(self.df), 2)

    def test_columns_df(self):
        self.assertEqual(self.df.columns.tolist(), self.columns)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSpark))
    # or you can add specific function with the following:
    # suite.addTest(TestSpark('test_len_df'))
    # suite.addTest(TestSpark('test_columns_df'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
