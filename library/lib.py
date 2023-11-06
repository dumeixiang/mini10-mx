from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as F

def init_spark(app_name: str, memory: str = "2g") -> SparkSession:
    session = SparkSession.builder.appName(app_name) \
        .config("session.executor.memory", memory) \
        .getOrCreate()
    return session

def read_csv(session: SparkSession, file_path: str) -> DataFrame:
    data_file = session.read.csv(file_path, header=True, inferSchema=True)
    return data_file

def spark_sql_query(spark: SparkSession, data: DataFrame):
    # create tempviw
    data.createOrReplaceTempView("Crime_Data_de")
    
    # Spark SQL to group by
    result = spark.sql("""
        SELECT Vict_Sex, 
               mean(Vict_Age) as mean_vic_age, 
               max(Vict_Age) as max_vic_age
        FROM Crime_Date_de
        GROUP BY Vict_Sex
    """)
    result.show()
    return result

def transform(spark: SparkSession, data: DataFrame) -> DataFrame:
    # create transform column
    conditions = [
        (F.col("Vict_Age") < 18, "y"),
        (F.col("Vict_Age") >= 19, "n")
    ]
    return data.withColumn("ifchild", F.when(conditions[0][0], conditions[0][1]).otherwise(conditions[1][1]))

