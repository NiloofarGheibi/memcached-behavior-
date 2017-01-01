FROM ubuntu:16.04
      
MAINTAINER Niloofar Gheibi <niloofar.gheibi@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

#SSH SERVER + R

RUN apt-get update && apt-get install -y openssh-server mercurial build-essential r-base
RUN mkdir /var/run/sshd

#RUN apt-get update && apt-get install -y openssh-server
#RUN mkdir /var/run/sshd
#RUN echo 'root:screencast' | chpasswd
#RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

#ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

COPY sshd_config /etc/ssh/sshd_config
COPY id_rsa.pub /root/.ssh/authorized_keys
COPY id_rsa /root/.ssh/

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

#dude
RUN hg clone https://bitbucket.org/db7/dude
WORKDIR dude/
RUN python setup.py install

WORKDIR ..

COPY Dudefile /
COPY Benchmark.py /
COPY graphs.R /

COPY run.sh /
RUN chmod 777 /run.sh

EXPOSE 10023

CMD ["/usr/sbin/sshd", "-D"]
