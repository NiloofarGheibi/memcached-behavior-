library(lattice)

#read.table("output-throughput-latency/stats.csv", header=TRUE) -> csvDataFrameSource
#csvDataFrame <- csvDataFrameSource

read.table("result.csv", header=TRUE, ",") -> csvDataFrameSource
csvDataFrame <- csvDataFrameSource
csvDataFrameSource

trellis.device("pdf", file="graph1.pdf", color=T, width=6.5, height=5.0)

# ... xyplot here

plot(csvDataFrameSource$rate,csvDataFrameSource$requests,type="o",ylab="Response Rate",xlab="Throughput")

dev.off() -> null 

trellis.device("pdf", file="graph2.pdf", color=T, width=6.5, height=5.0)

# ... xyplot here

plot(csvDataFrameSource$requests,csvDataFrameSource$latency,type="o",ylab="Latency",xlab="Throughput")
plot(csvDataFrameSource$requests,csvDataFrameSource$max_latency,type="o",ylab="Latency",xlab="Throughput")
plot(csvDataFrameSource$requests,csvDataFrameSource$min_latency,type="o",ylab="Latency",xlab="Throughput")
dev.off() -> null 
