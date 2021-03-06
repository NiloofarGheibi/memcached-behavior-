FROM ubuntu:16.04
      
MAINTAINER Niloofar Gheibi <niloofar.gheibi@mailbox.tu-dresden.de>

RUN groupadd -r memcache && useradd -r -g memcache memcache

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

COPY sshd_config /etc/ssh/sshd_config
COPY id_rsa.pub /root/.ssh/authorized_keys

RUN apt-get update && apt-get install -y --no-install-recommends \
		libevent-2.0-5 \
	&& rm -rf /var/lib/apt/lists/*

ENV MEMCACHED_VERSION 1.4.33
ENV MEMCACHED_SHA1 e343530c55946ccbdd78c488355b02eaf90b3b46

RUN buildDeps=' \
		gcc \
		libc6-dev \
		libevent-dev \
		make \
		perl \
		wget \
	' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& wget -O memcached.tar.gz "http://memcached.org/files/memcached-$MEMCACHED_VERSION.tar.gz" \
	&& echo "$MEMCACHED_SHA1  memcached.tar.gz" | sha1sum -c - \
	&& mkdir -p /usr/src/memcached \
	&& tar -xzf memcached.tar.gz -C /usr/src/memcached --strip-components=1 \
	&& rm memcached.tar.gz \
	&& cd /usr/src/memcached \
	&& ./configure \
	&& make -j$(nproc) \
	&& make install \
	&& cd / && rm -rf /usr/src/memcached \
	&& apt-get purge -y --auto-remove $buildDeps

RUN mkdir mm
RUN chmod 777 /mm

EXPOSE 10022 11211
CMD ["/usr/sbin/sshd", "-D"]
