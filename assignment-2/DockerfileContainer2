FROM ubuntu:16.04
      
MAINTAINER Niloofar Gheibi <niloofar.gheibi@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN sed -i 's/Port 22/Port 10023/' /etc/ssh/sshd_config

RUN apt-get install git -y
RUN apt-get install autoconf -y
RUN apt-get install build-essential -y

RUN git clone git://github.com/twitter/twemperf.git\
&& cd twemperf\
&& autoreconf -fvi\
&& CFLAGS="-ggdb3 -O0" ./configure --enable-debug\
&& make\
&& src/mcperf -h

COPY Dudefile /
COPY Benchmark.py /

EXPOSE 10023

CMD ["-m", "128"]

USER daemon
  
ENTRYPOINT mcperf