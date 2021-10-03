import matplotlib.pyplot as plt
import subprocess
import time
import sys
import os

# Thresholds in %
threshold = [5,10,25,50,95]

# Start time for each Threshold
start_time_fsg = []
# start_time_ = []
# start_time_ = []

# End time for each Threshold
end_time_fsg = []
# end_time_ = []
# end_time_ = []

# Preprocessing of the data file for FSG
print("Processing the file for FSG")
print("./Q1/FSG/script_fsg",str(sys.argv[1]),"/Q1/FSG/data_file.txt")
subprocess.run(["./Q1/FSG/script_fsg",sys.argv[1],"/Q1/FSG/data_file.txt"])
print("Processing of the file completed")


for i in threshold:
	start_time_fsg.append(time.time())
	subprocess.run(["./Q1/FSG/fsg","-s",str(i),"/Q1/FSG/data_file.txt"])
	end_time_fsg.append(time.time())

'''
for i in threshold2:
	start_time_apriori.append(time.time())
	subprocess.run(["./part2a/apriori",sys.argv[1],str(i),"output/output_apriori_"+str(i)+".txt"])
	end_time_apriori.append(time.time())

'''
time_fsg=[]

for i in range(len(threshold)):
	time_fsg.append(end_time_fsg[i] - start_time_fsg[i])


plt.plot(threshold,time_fsg,'-r',label = 'FSG')

plt.xlabel('Support threshold %')
plt.ylabel('Running time (sec)')

plt.legend(loc='upper right')
plt.title('Support threshold vs running time for FSG')

plt.savefig(sys.argv[2])
