import unittest
from spark_application.util.spark import init_spark
import databricks.koalas as ks


class TestSpark(unittest.TestCase):
    def test_simple_dataframe(self):
        dataset = [("abc", 1), ("def", 2)]
        columns = ["name", "age"]
        spark, sc = init_spark()
        source_df = ks.DataFrame(data=dataset, columns=columns)
        self.assertEqual(len(source_df), 2)
        self.assertEqual(source_df.columns.tolist(), columns)


if __name__ == "__main__":
    unittest.main()
