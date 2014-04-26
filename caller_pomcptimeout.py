import os
import csv

displacements = [2.00, 1.75, 1.50, 1.25, 1.00, 0.75, 0.50, 0.25, 0.00]

# for i in range(1):
# 	for j in range(9):
# 		with open("status_pomcptimeout50-"+str(j)+".csv", 'a') as fp:
# 			a = csv.writer(fp, delimiter=',')
# 			data = [["i","agent_pomcptimeout"],[i,50]]
# 			a.writerows(data)
# 		os.system("python corobots5_pomcptimeout.py 50 "+str(displacements[j])+" 25 1 "+str(j)+" &")



for i in range(1):
	for j in range(9):
		with open("status_pomcptimeout100-"+str(j)+".csv", 'a') as fp:
			a = csv.writer(fp, delimiter=',')
			data = [["i","agent_pomcptimeout"],[i,100]]
			a.writerows(data)
		os.system("python corobots5_pomcptimeout.py 100 "+str(displacements[j])+" 25 1 "+str(j)+" &")



# for i in range(1):
# 	for j in range(9):
# 		with open("status_pomcptimeout150-"+str(j)+".csv", 'a') as fp:
# 			a = csv.writer(fp, delimiter=',')
# 			data = [["i","agent_pomcptimeout"],[i,150]]
# 			a.writerows(data)
# 		os.system("python corobots5_pomcptimeout.py 150 "+str(displacements[j])+" 25 1 "+str(j)+" &")
