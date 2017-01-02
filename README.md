# README #

Instructions to see the result of project testing behavior of memcached while receiving requests via [mcperf](https://github.com/twitter/twemperf)

### What is this repository for? ###

* Course Project of System Engineering 1. 
The purpose of the project working with scripts, running experiments and get familiar with docker containers.
Drawing graphs via R graphics
* version 1

### How do I get set up? ###


```
#!script

sudo docker build -t server-image Container1
```

```
#!script

sudo docker build -t client-image Container2
```

```
#!script

docker run -p 10022:10022 --name server server-image
```
```
#!script

docker run -p 10023:10023 --link server:server --name client client-image
```

```
#!script

ssh 127.0.0.1 -p 10023
```
```
#!script

cd ..
```

```
#!script

sh run.sh
```

In the terminal of the Host:

```
#!script

docker cp <client-ID>:/graph1.pdf Path/in/Host/graphs/
```

```
#!script

docker cp <client-ID>:/graph2.pdf Path/in/Host/graphs/
```

### Results with Different mcperf Parametes ###

In mcperf 

* --num-calls=6 --num-conns=50
![Screen Shot 2017-01-02 at 19.07.18.png](https://bitbucket.org/repo/Gxrn8e/images/2184891254-Screen%20Shot%202017-01-02%20at%2019.07.18.png)

![Screen Shot 2017-01-02 at 19.07.31.png](https://bitbucket.org/repo/Gxrn8e/images/515344820-Screen%20Shot%202017-01-02%20at%2019.07.31.png)

* --num-calls=6 --num-conns=100

![Screen Shot 2017-01-02 at 19.09.05.png](https://bitbucket.org/repo/Gxrn8e/images/222449006-Screen%20Shot%202017-01-02%20at%2019.09.05.png)

![Screen Shot 2017-01-02 at 19.09.12.png](https://bitbucket.org/repo/Gxrn8e/images/2245210082-Screen%20Shot%202017-01-02%20at%2019.09.12.png)

* --num-calls=8 --num-conns=50
![Screen Shot 2017-01-02 at 19.10.26.png](https://bitbucket.org/repo/Gxrn8e/images/1011105538-Screen%20Shot%202017-01-02%20at%2019.10.26.png)

![Screen Shot 2017-01-02 at 19.10.35.png](https://bitbucket.org/repo/Gxrn8e/images/2993356580-Screen%20Shot%202017-01-02%20at%2019.10.35.png)

* --num-calls=8 --num-conns=100
![Screen Shot 2017-01-02 at 19.12.53.png](https://bitbucket.org/repo/Gxrn8e/images/3849876291-Screen%20Shot%202017-01-02%20at%2019.12.53.png)

![Screen Shot 2017-01-02 at 19.13.01.png](https://bitbucket.org/repo/Gxrn8e/images/477062597-Screen%20Shot%202017-01-02%20at%2019.13.01.png)

### Who do I talk to? ###

email me: niloofar.gheibi@gmail.com