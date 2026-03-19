import os
import sys
import pytest

# Run the tests from the root directory
sys.path.append(os.getcwd())

# Returning a Spark Session
@pytest.fixture()
def spark():
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
        print("Using DatabricksSession.")
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
            print("Using SparkSession.")
        except ImportError:
            raise ImportError("Neither DatabricksSession nor SparkSession Could be imported.")
        return spark