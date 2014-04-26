import os
import csv

displacements = [2.00, 1.75, 1.50, 1.25, 1.00, 0.75, 0.50, 0.25, 0.00]

for i in range(1):
	for j in range(9):
		with open("status_numcact"+str(j)+".csv", 'a') as fp:
			a = csv.writer(fp, delimiter=',')
			data = [["i","agent_numcact"],[i,5]]
			a.writerows(data)
		os.system("python corobots5_pomcptimeout.py 100 "+str(displacements[j])+" 5 0 "+str(j)+" &")

# for i in range(1):
# 	for j in range(9):
# 		with open("status_numcact"+str(j)+".csv", 'a') as fp:
# 			a = csv.writer(fp, delimiter=',')
# 			data = [["i","agent_numcact"],[i,15]]
# 			a.writerows(data)
# 		os.system("python corobots5_pomcptimeout.py 100 "+str(displacements[j])+" 15 0 "+str(j)+" &")

# for i in range(1):
# 	for j in range(9):
# 		with open("status_numcact"+str(j)+".csv", 'a') as fp:
# 			a = csv.writer(fp, delimiter=',')
# 			data = [["i","agent_numcact"],[i,25]]
# 			a.writerows(data)
# 		os.system("python corobots5_pomcptimeout.py 100 "+str(displacements[j])+" 25 0 "+str(j)+" &")