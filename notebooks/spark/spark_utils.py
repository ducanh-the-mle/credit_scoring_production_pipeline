import os
from pyspark.sql import SparkSession


class CustomSparkSession:
    def __init__(self, app_name: str = "MinIODataExploration"):
        self.app_name = app_name
        self.spark = None

    def create_session(self) -> SparkSession:
        self.spark = (
            SparkSession.builder
            .appName(self.app_name)
            .master(os.environ["SPARK_MASTER"])
            .config(
                "spark.hadoop.fs.s3a.endpoint",
                os.environ["MINIO_ENDPOINT"]
            )
            .config(
                "spark.hadoop.fs.s3a.access.key",
                os.environ["AWS_ACCESS_KEY_ID"]
            )
            .config(
                "spark.hadoop.fs.s3a.secret.key",
                os.environ["AWS_SECRET_ACCESS_KEY"]
            )
            .config("spark.hadoop.fs.s3a.path.style.access", "true")
            .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
            .config(
                "spark.hadoop.fs.s3a.impl",
                "org.apache.hadoop.fs.s3a.S3AFileSystem"
            )
            .getOrCreate()
        )

        return self.spark

    def stop_session(self) -> None:
        if self.spark is not None:
            self.spark.stop()
            self.spark = None