import os
import csv

for i in range(5):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,5]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 25 0")
	os.system("python corobots5_pomcptimeout.py 100 0.4 25 0")
	os.system("python corobots5_pomcptimeout.py 100 0.6 25 0")
	os.system("python corobots5_pomcptimeout.py 100 0.8 25 0")
	os.system("python corobots5_pomcptimeout.py 100 1.0 25 0")

for i in range(5):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,10]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 20 0")
	os.system("python corobots5_pomcptimeout.py 100 0.4 20 0")
	os.system("python corobots5_pomcptimeout.py 100 0.6 20 0")
	os.system("python corobots5_pomcptimeout.py 100 0.8 20 0")
	os.system("python corobots5_pomcptimeout.py 100 1.0 20 0")

for i in range(5):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,15]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 15 0")
	os.system("python corobots5_pomcptimeout.py 100 0.4 15 0")
	os.system("python corobots5_pomcptimeout.py 100 0.6 15 0")
	os.system("python corobots5_pomcptimeout.py 100 0.8 15 0")
	os.system("python corobots5_pomcptimeout.py 100 1.0 15 0")

for i in range(5):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,20]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 10 0")
	os.system("python corobots5_pomcptimeout.py 100 0.4 10 0")
	os.system("python corobots5_pomcptimeout.py 100 0.6 10 0")
	os.system("python corobots5_pomcptimeout.py 100 0.8 10 0")
	os.system("python corobots5_pomcptimeout.py 100 1.0 10 0")

for i in range(5):
	with open('status_numcact.csv', 'a') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [["i","agent_numcact"],[i,25]]
		a.writerows(data)
	os.system("python corobots5_pomcptimeout.py 100 0.2 5 0")
	os.system("python corobots5_pomcptimeout.py 100 0.4 5 0")
	os.system("python corobots5_pomcptimeout.py 100 0.6 5 0")
	os.system("python corobots5_pomcptimeout.py 100 0.8 5 0")
	os.system("python corobots5_pomcptimeout.py 100 1.0 5 0")
