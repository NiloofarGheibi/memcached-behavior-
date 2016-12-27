FROM ubuntu:16.04
      
MAINTAINER Niloofar Gheibi <niloofar.gheibi@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get update && apt-get install -y memcached
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/ssh
RUN sed -i 's/Port 22/Port 10022/' /etc/ssh/sshd_config
RUN sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config


#RUN echo 'root:screencast' | chpasswd
#RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 10022 11211
CMD ["/usr/sbin/sshd", "-D"]
ENTRYPOINT ["start.sh"]