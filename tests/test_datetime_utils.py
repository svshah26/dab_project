import datetime

from src.utils.datetime_utils import timestamp_to_date_col

def test_timestamp_to_date_col(spark):
    
    data = [(datetime.datetime(2025, 4, 10, 10, 30, 0),)]
    schema = "ride_timestamp timestamp"
    df = spark.createDataFrame(data, schema=schema)

    result_df = timestamp_to_date_col(spark, df, "ride_timestamp", "ride_date")

    row = result_df.select("ride_date").first()
    expected_date = datetime.date(2025, 4, 10)

    assert row["ride_date"] == expected_date

    spark.stop()