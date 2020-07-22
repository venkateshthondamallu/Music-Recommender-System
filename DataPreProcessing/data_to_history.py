import csv
import numpy as np 

file = "user_history.csv"
data = []
j=0
with open(file,'r') as csvfile:
	csvreader = csv.reader(csvfile)

	for row in csvreader:
		if(j%2==0):
			data.append(row)
		j=j+1

np_arr = np.array(data)

users = np_arr[:,0]

print(len(users))
users_uni = np.unique(users)
songs = np_arr[:,1]
#create a list for every user

file = "history.csv"

with open(file,'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	for i in range(0,len(users_uni)):
		l=users_uni[i]
		lis = []
		lis.append(l)
		indexes = np.where(users==l)
		lis.extend(songs[indexes])
		csvwriter.writerow(lis)

