
FROM python:3.11-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG HADOOP_VERSION=3.3.4
ARG AWS_SDK_VERSION=1.12.262

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

RUN pip install --no-cache-dir \
    jupyterlab \
    pyspark==3.5.1 \
    pandas \
    numpy \
    pyarrow \
    boto3 \
    s3fs \
    xgboost \
    scikit-learn \
    joblib 

# Add S3A dependencies to the notebook's own Spark classpath.
RUN set -eux; \
    SPARK_JARS="$(python -c 'import pyspark, os; print(os.path.join(pyspark.__path__[0], "jars"))')"; \
    curl -fL --retry 3 \
      "https://repo.maven.apache.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar" \
      -o "${SPARK_JARS}/hadoop-aws-${HADOOP_VERSION}.jar"; \
    curl -fL --retry 3 \
      "https://repo.maven.apache.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar" \
      -o "${SPARK_JARS}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar"; \
    chmod 644 \
      "${SPARK_JARS}/hadoop-aws-${HADOOP_VERSION}.jar" \
      "${SPARK_JARS}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar"

RUN useradd -m -s /bin/bash jovyan \
    && mkdir -p /home/jovyan/work \
    && chown -R jovyan:jovyan /home/jovyan

USER jovyan
WORKDIR /home/jovyan/work

EXPOSE 8888

CMD ["sh", "-c", "jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --ServerApp.token=${JUPYTER_TOKEN}"]
