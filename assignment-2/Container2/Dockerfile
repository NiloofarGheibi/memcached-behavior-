FROM ubuntu:16.04
      
MAINTAINER Niloofar Gheibi <niloofar.gheibi@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN sed -i 's/Port 22/Port 10023/' /etc/ssh/sshd_config


#RUN apt-get install wget -y

#RUN wget mcperf-0.1.1.tar.gz "https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/twemperf/mcperf-0.1.1.tar.gz" \
 #&& mkdir -p /usr/src/mcperf \
 #&& tar -xzf mcperf-0.1.1.tar.gz -C /usr/src/mcperf --strip-components=1 \
 #&& rm mcperf-0.1.1.tar.gz \
 #&& cd /usr/src/mcperf \
 #&& make \
 #&& make install \
 #&& cd / \
 #&& rm -rf /usr/src/mcperf

RUN apt-get install git -y
RUN apt-get install autoconf -y

RUN git clone git://github.com/twitter/twemperf.git
RUN cd twemperf
RUN autoreconf -fvi
RUN CFLAGS="-ggdb3 -O0" ./configure --enable-debug
RUN make
RUN src/mcperf -h
RUN cd /

COPY Dudefile /
COPY Benchmark.py /

EXPOSE 10023

CMD ["-m", "128"]

USER daemon
  
ENTRYPOINT mcperf