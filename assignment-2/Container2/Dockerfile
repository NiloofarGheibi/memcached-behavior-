FROM ubuntu:16.04
      
MAINTAINER Niloofar Gheibi <niloofar.gheibi@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

#SSH SERVER + R

RUN apt-get update && apt-get install -y openssh-server mercurial build-essential r-base
RUN mkdir /var/run/sshd



COPY sshd_config /etc/ssh/sshd_config
COPY id_rsa.pub /root/.ssh/authorized_keys
COPY id_rsa /root/.ssh/


# Install mcperf
ADD https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/twemperf/mcperf-0.1.1.tar.gz /
RUN tar xf mcperf-0.1.1.tar.gz
WORKDIR /mcperf-0.1.1
RUN ./configure && make && make install

#dude
RUN hg clone https://bitbucket.org/db7/dude
WORKDIR dude/
RUN python setup.py install

WORKDIR ..

COPY Dudefile /
COPY Benchmark.py /
COPY graphs.R /

COPY run.sh /
COPY sum.py /
RUN chmod 777 /run.sh

EXPOSE 10023

CMD ["/usr/sbin/sshd", "-D"]
