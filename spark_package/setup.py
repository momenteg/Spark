from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()



setup(name='Spark_template',
      version='0.0.1',
      description='A template for a pyspark application',
      author='Giulio Momente',
      author_email='momenteg@gmail.com',
      packages=['spark_application'],
      zip_safe=False,
      install_requires=requirements,
      )