import os
import csv

for i in range(50):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,5]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 5")
	os.system("python corobots5_pomcptimeout.py 100 0.4 5")
	os.system("python corobots5_pomcptimeout.py 100 0.6 5")
	os.system("python corobots5_pomcptimeout.py 100 0.8 5")
	os.system("python corobots5_pomcptimeout.py 100 1.0 5")

for i in range(50):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,10]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 10")
	os.system("python corobots5_pomcptimeout.py 100 0.4 10")
	os.system("python corobots5_pomcptimeout.py 100 0.6 10")
	os.system("python corobots5_pomcptimeout.py 100 0.8 10")
	os.system("python corobots5_pomcptimeout.py 100 1.0 10")

for i in range(50):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,15]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 15")
	os.system("python corobots5_pomcptimeout.py 100 0.4 15")
	os.system("python corobots5_pomcptimeout.py 100 0.6 15")
	os.system("python corobots5_pomcptimeout.py 100 0.8 15")
	os.system("python corobots5_pomcptimeout.py 100 1.0 15")

for i in range(50):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,20]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 20")
	os.system("python corobots5_pomcptimeout.py 100 0.4 20")
	os.system("python corobots5_pomcptimeout.py 100 0.6 20")
	os.system("python corobots5_pomcptimeout.py 100 0.8 20")
	os.system("python corobots5_pomcptimeout.py 100 1.0 20")

for i in range(50):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,25]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 25")
	os.system("python corobots5_pomcptimeout.py 100 0.4 25")
	os.system("python corobots5_pomcptimeout.py 100 0.6 25")
	os.system("python corobots5_pomcptimeout.py 100 0.8 25")
	os.system("python corobots5_pomcptimeout.py 100 1.0 25")
