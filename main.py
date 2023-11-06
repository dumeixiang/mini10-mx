from library.lib import init_spark, read_csv, spark_sql_query, transform


if __name__ == "__main__":
    spark = init_spark(app_name="PySpark Data Processing")

    csv_file_path = "Crime_Data_de.csv"
    df = read_csv(spark, csv_file_path)

    # print raw data
    print("Original Data:")
    df.show()

    # Spark SQL based data print 
    print("Data After Spark SQL Query:")
    spark_sql_query(spark, df)

    #  
    df_with_category = transform(spark, df)
    print("Data After Adding Bill Length Category:")
    df_with_category.show()
