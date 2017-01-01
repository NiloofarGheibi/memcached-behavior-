import os
import stat

def prepare_exp(SSHHost, SSHPort, REMOTEROOT, optpt):
    f = open("config", 'w')
    f.write("Host benchmark\n")
    f.write("   Hostname %s\n" % SSHHost)
    f.write("   Port %d\n" % SSHPort)
    f.close()
    

    f.write("   IdentityFile /root/.ssh/id_rsa\n")
    f.write("   StrictHostKeyChecking no\n")
    f.close()

    f = open("run-experiment.sh", 'w')
    f.write("#!/bin/bash\n")
    f.write("set -x\n\n")
    
   #f.write("ssh -F config benchmark \"nohup ls dummy -p 11222 -P memcached.pid > memcached.out 2> memcached.err &\"\n") # adjust this line to properly start memcached
    
    f.write("ssh -F config benchmark \"memcached -d -u memcache -P /mm/memcached.pid > /mm/memcached.out 2> /mm/memcached.err &\"\n")

    f.write("RESULT=`ssh -F config benchmark \"pidof memcachd\"`\n")

    f.write("sleep 5\n")

    f.write("if [[ -z \"${RESULT// }\" ]]; then echo \"memcached process not running\"; CODE=1; else CODE=0; fi\n")
        
    #f.write("%s/ummy --execute-number=%d --concurrency=%d -s %s > stats.log\n\n" % (REMOTEROOT, optpt["noRequests"], optpt["concurrency"], SSHHost)) #adjust this line to properly start the client
    
    # add a few lines to extract the "Response rate" and "Response time \[ms\]: av and store them in $REQPERSEC and $LATENCY"
	
    f.write("mcperf --linger=0 --timeout=5 --conn-rate=%d --call-rate=1000 --num-calls=6 --num-conns=50 --sizes=u1,16 2>outputest_%d.txt\n" % (optpt["rate"], optpt["rate"]))

    f.write("REQPERSEC=$(cat outputest_%d.txt | grep \"Response rate:\" | cut -c16- | sed 's/ .*//')\n" % (optpt["rate"]) )

    f.write("LATENCY=$(cat outputest_%d.txt | grep \"Response time \[ms]: avg\" | cut -c25- | sed 's/ .*//')\n" % (optpt["rate"]))

    f.write("MAX_LATENCY=$(cat outputest_%d.txt | grep \"Response time \[ms]: p95\" | cut -c25- | sed 's/ .*//')\n" % (optpt["rate"]))

    f.write("MIN_LATENCY=$(cat outputest_%d.txt | grep \"Response time \[ms]: p25\" | cut -c25- | sed 's/ .*//')\n" % (optpt["rate"]))

    f.write("ssh -F config benchmark \"sudo kill -9 $(cat /mm/memcached.pid)\"\n")

    f.write("echo \"requests,latency,max_latency,min_latency\" > stats.csv\n")
    
    f.write("echo \"$REQPERSEC,$LATENCY,$MAX_LATENCY,$MIN_LATENCY\" >> stats.csv\n")
    
    f.write("scp -F config benchmark:~/mm/memcached.* .\n")

    f.write("if [[ $(wc -l <stats.csv) -le 1 ]]; then CODE=1; fi\n\n")
    
    f.write("exit $CODE\n")

    f.close()
    
    os.chmod("run-experiment.sh", stat.S_IRWXU) 

def finish_exp(optpt):

	result_string = "" 

	for output_rate in [1000, 2000, 5000, 10000, 20000, 30000, 50000, 100000, 150000] :
		filename = "/home/niloofar/Desktop/SE1_HW2/assignment-2/raw-throughput-latency/exp__rate" + str(output_rate) + "/stats.csv"
		with open(filename) as fp:
			for i, line in enumerate(fp):
				if i == 2:
					result_string += line.strip() + "\n"
	print(result_string)
	# adding all results into a single result file.
	with open("result.csv", "w") as outputfile:
		outputfile.write("rate, requests, latency, max_latency, min_latency\n" + result_string)

		


		
 

	
