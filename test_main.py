from library.lib import init_spark, read_csv, spark_sql_query, transform
from pyspark.sql import SparkSession, Row


def test_init_spark():
    spark = init_spark(app_name="PySpark Data Processing")
    assert isinstance(spark, SparkSession), "Test failed."
    print("Test initiation spark passed successfully.")


def test_read_csv():
    spark = init_spark(app_name="PySpark Data Processing")
    csv_file_path = "Crime_Data_de.csv"
    df = read_csv(spark, csv_file_path)
    print(df)
    assert df.count() > 0, "Test failed."
    print("Test reading csv file passed successfully.")

if __name__ == "__main__":
    test_init_spark()
    test_read_csv()
