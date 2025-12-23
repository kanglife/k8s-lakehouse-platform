from pyspark.sql import SparkSession

print("FILE LOADED")

if __name__ == "__main__":
    print("MAIN STARTED")

    spark = (
        SparkSession.builder
        .appName("Sprint3-Raw-To-Parquet")
        .master("local[*]")
        .getOrCreate()
    )

    print("SparkSession created")

    df = spark.read.json("data/raw/sample.ndjson")

    print("Schema:")
    df.printSchema()

    print("Preview:")
    df.show(5)

    df.write.mode("overwrite").parquet("data/processed/sample_parquet")

    print("Parquet write completed")

    spark.stop()
