#How to develop locally with pyspark:

- install anaconda
- install pyspark 
- download and unzip spark release https://spark.apache.org/downloads.html
- add `export SPARK_HOME=~/spark-3.1.1-bin-hadoop2.7` to your bashrc


### How to run unit tests:
`python -m unittest tests/test_spark.py`

## How to build the package: 
`python setup.py bdist_wheel`