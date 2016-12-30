FROM ubuntu:16.04
      
MAINTAINER Niloofar Gheibi <niloofar.gheibi@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

#mcperf
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

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
