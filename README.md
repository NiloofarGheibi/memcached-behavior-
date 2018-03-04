# README #

Instructions to see the result of project testing behavior of memcached while receiving requests via [mcperf](https://github.com/twitter/twemperf)

## Important Note ##
for Testing the Project you should make public/private key for authentication reasons and copy them into Container1 and Container2 Folders, Now it's my public/private keys.

### What is this repository for? ###

* Course Project of System Engineering 1. 
The purpose of the project working with scripts, running experiments and get familiar with docker containers.
Drawing graphs via R graphics 


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

ssh 127.0.0.1 -p 10023 "cd ..; sh run.sh"
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
![--num-calls=6 --num-conns=50](https://github.com/NiloofarGheibi/memcached-behavior-/blob/master/screenshots/--num-calls%3D6%20--num-conns%3D50.png)


![--num-calls=6 --num-conns=50-latency](https://github.com/NiloofarGheibi/memcached-behavior-/blob/master/screenshots/--num-calls%3D6%20--num-conns%3D50-latency.png)

* --num-calls=6 --num-conns=100

![-num-calls=6 --num-conns=100](https://github.com/NiloofarGheibi/memcached-behavior-/blob/master/screenshots/--num-calls%3D6%20--num-conns%3D100.png)

![-num-calls=6 --num-conns=100-latency](https://github.com/NiloofarGheibi/memcached-behavior-/blob/master/screenshots/--num-calls%3D6%20--num-conns%3D100-latency.png)

* --num-calls=8 --num-conns=50
![--num-calls=8 --num-conns=50](https://github.com/NiloofarGheibi/memcached-behavior-/blob/master/screenshots/--num-calls%3D8%20--num-conns%3D50.png)

![--num-calls=8 --num-conns=50-latency](https://github.com/NiloofarGheibi/memcached-behavior-/blob/master/screenshots/--num-calls%3D8%20--num-conns%3D50-latency.png)

* --num-calls=8 --num-conns=100
![--num-calls=8 --num-conns=100](https://github.com/NiloofarGheibi/memcached-behavior-/blob/master/screenshots/--num-calls%3D8%20--num-conns%3D100%20.png)

![--num-calls=8 --num-conns=100](https://github.com/NiloofarGheibi/memcached-behavior-/blob/master/screenshots/--num-calls%3D8%20--num-conns%3D100-latency.png)

### Who do I talk to? ###

email me: niloofar.gheibi@gmail.com