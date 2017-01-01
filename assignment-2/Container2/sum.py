result_string = "" 

for output_rate in [1000, 2000, 5000, 10000, 20000, 30000, 50000, 100000, 150000] :
	filename = "/home/niloofar/Desktop/SE1_HW2/assignment-2/raw-throughput-latency/exp__rate" + str(output_rate) + "/stats.csv"
	with open(filename) as fp:
		for i, line in enumerate(fp):
			print (str(i))
			if i == 1:
				print( line.strip() )
				result_string += str(output_rate) + "," + line.strip() + "\n"
	


print(result_string)
# adding all results into a single result file.
with open("result.csv", "w") as outputfile:
	outputfile.write("rate, requests, latency, max_latency, min_latency\n" + result_string)
