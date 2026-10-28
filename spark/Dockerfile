FROM apache/spark:3.5.1

USER root

ARG HADOOP_VERSION=3.3.4
ARG AWS_SDK_VERSION=1.12.262

ADD https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar \
    /opt/spark/jars/hadoop-aws-${HADOOP_VERSION}.jar

ADD https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar \
    /opt/spark/jars/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar

RUN chmod 644 \
    /opt/spark/jars/hadoop-aws-${HADOOP_VERSION}.jar \
    /opt/spark/jars/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar

USER spark

EXPOSE 7077 8080 8081