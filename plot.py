import matplotlib.pyplot as plt
import subprocess
import time
import sys
import os

# Thresholds in %
threshold = [90,70,60,50,30,25,10]
threshold2 = [90,70,60,50,25]

# Start time for each Threshold
start_time_apriori = []
start_time_fpgrowth = []

# End time for each Threshold
end_time_apriori = []
end_time_fpgrowth = []

for i in threshold:
	start_time_fpgrowth.append(time.time())
	subprocess.run(["./part2b/fpgrowth/fpgrowth/src/fpgrowth","-s"+str(i),sys.argv[1],"output/output_fp_"+str(i)+".txt"])
	end_time_fpgrowth.append(time.time())

for i in threshold2:
	start_time_apriori.append(time.time())
	subprocess.run(["./part2a/apriori",sys.argv[1],str(i),"output/output_apriori_"+str(i)+".txt"])
	end_time_apriori.append(time.time())

time_apriori=[]
time_fpgrowth = []
for i in range(len(threshold2)):
	time_apriori.append(end_time_apriori[i] - start_time_apriori[i])

for i in range(len(threshold)):
	time_fpgrowth.append(end_time_fpgrowth[i] - start_time_fpgrowth[i])

threshold.reverse()
threshold2.reverse()
time_apriori.reverse()
time_fpgrowth.reverse()

plt.plot(threshold2,time_apriori,'-r',label = 'Apriori')
plt.plot(threshold,time_fpgrowth,'-b',label = 'Fpgrowth')

plt.xlabel('Support threshold %')
plt.ylabel('Running time (sec)')

plt.legend(loc='upper right')
plt.title('Support threshold vs running time for apriori and fptree')

plt.savefig("output/plot.png")
