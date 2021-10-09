import matplotlib.pyplot as plt
import subprocess
import time
import sys
import os

# Thresholds in %
threshold = [5,10,25,50,95]

# Start time for each Threshold
start_time_fsg = []
start_time_gaston = []
start_time_gspan = []

# End time for each Threshold
end_time_fsg = []
end_time_gaston = []
end_time_gspan = []

# Preprocessing of the data file for FSG
print("Processing the file for FSG")
subprocess.run(["./Q1/FSG/script_fsg",sys.argv[1],"Q1/FSG/data_file.txt"])
print("Processing the file for Gaston")
subprocess.run(["./Q1/Gaston/script_gaston",sys.argv[1],"Q1/Gaston/data_file.txt"])
print("Processing the file for gSpan")
subprocess.run(["./Q1/gSpan/script_gspan",sys.argv[1],"Q1/gSpan/data_file.txt"])
print("Processing of the file completed")

for i in threshold:
        start_time_gspan.append(time.time())
        subprocess.run(["./Q1/gSpan/gSpan-64","-s",str(i/100),"-f","Q1/gSpan/data_file.txt"])
        end_time_gspan.append(time.time())

for i in threshold:
	start_time_fsg.append(time.time())
	subprocess.run(["./Q1/FSG/fsg","-s",str(i),"Q1/FSG/data_file.txt"])
	end_time_fsg.append(time.time())

for i in threshold:
        start_time_gaston.append(time.time())
        subprocess.run(["./Q1/Gaston/gaston",str(i),"Q1/Gaston/data_file.txt"])
        end_time_gaston.append(time.time())

'''
for i in threshold2:
	start_time_apriori.append(time.time())
	subprocess.run(["./part2a/apriori",sys.argv[1],str(i),"output/output_apriori_"+str(i)+".txt"])
	end_time_apriori.append(time.time())

'''

time_gspan=[]

for i in range(len(threshold)):
        time_gspan.append(end_time_gspan[i] - start_time_gspan[i])

time_fsg=[]

for i in range(len(threshold)):
	time_fsg.append(end_time_fsg[i] - start_time_fsg[i])

time_gaston=[]

for i in range(len(threshold)):
        time_gaston.append(end_time_gaston[i] - start_time_gaston[i])

plt.plot(threshold,time_gspan,'-b',label = 'gSpan')
plt.plot(threshold,time_fsg,'-g',label = 'FSG')
plt.plot(threshold,time_gaston,'-r',label = 'Gaston')

plt.xlabel('Support threshold %')
plt.ylabel('Running time (sec)')

plt.legend(loc='upper right')
plt.title('Support threshold vs running time')

plt.savefig(sys.argv[2])
