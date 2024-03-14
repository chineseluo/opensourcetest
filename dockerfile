FROM python:3.9
RUN pip3 install --upgrade opensourcetest -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get update
RUN cd /usr/local && wget https://mirrors.huaweicloud.com/java/jdk/8u191-b12/jdk-8u191-linux-x64.tar.gz && tar -zxvf jdk-8u191-linux-x64.tar.gz
ENV JAVA_HOME /usr/local/jdk1.8.0_191
ENV PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
RUN wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.27.0/allure-commandline-2.27.0.zip && unzip allure-commandline-2.27.0.zip
ENV PATH=$PATH:/allure-2.27.0/bin
CMD ["python","--version"]