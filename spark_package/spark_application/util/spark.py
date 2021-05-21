import findspark

findspark.init()

from pyspark.sql import SparkSession


def init_spark():
    spark = SparkSession.builder.master("local[4]").appName("spark_application").getOrCreate()
    sc = spark.sparkContext
    return spark, sc
