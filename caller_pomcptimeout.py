import os
import csv

for i in range(50):
	with open('status_pomcptimeout.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_pomcptimeout"],[i,50]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 50 0.2 25")
	os.system("python corobots5_pomcptimeout.py 50 0.4 25")
	os.system("python corobots5_pomcptimeout.py 50 0.6 25")
	os.system("python corobots5_pomcptimeout.py 50 0.8 25")
	os.system("python corobots5_pomcptimeout.py 50 1.0 25")

# for i in range(50):
# 	with open('status_pomcptimeout.csv', 'a') as fp:
# 		a = csv.writer(fp, delimiter=',')
# 		data = [["i","agent_pomcptimeout"],[i,100]]
# 		a.writerows(data)
# 	os.system("python corobots5_pomcptimeout.py 100 0.2 25")
# 	os.system("python corobots5_pomcptimeout.py 100 0.4 25")
# 	os.system("python corobots5_pomcptimeout.py 100 0.6 25")
# 	os.system("python corobots5_pomcptimeout.py 100 0.8 25")
# 	os.system("python corobots5_pomcptimeout.py 100 1.0 25")

# for i in range(50):
# 	with open('status_pomcptimeout.csv', 'a') as fp:
# 		a = csv.writer(fp, delimiter=',')
# 		data = [["i","agent_pomcptimeout"],[i,150]]
# 		a.writerows(data)
# 	os.system("python corobots5_pomcptimeout.py 150 0.2 25")
# 	os.system("python corobots5_pomcptimeout.py 150 0.4 25")
# 	os.system("python corobots5_pomcptimeout.py 150 0.6 25")
# 	os.system("python corobots5_pomcptimeout.py 150 0.8 25")
# 	os.system("python corobots5_pomcptimeout.py 150 1.0 25")
