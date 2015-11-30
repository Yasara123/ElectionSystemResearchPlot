import MySQLdb
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np
import csv
import warnings

    #writer.writerow({'Rank': 'Baked', 'RTweet_Fvrt': 'Beans', 'Life_time': 'Beans'})




# Open database connection
db = MySQLdb.connect("localhost","root","sri","twitterDB" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "SELECT Rt,Ft ,diff,rank FROM data"
count=[]
Tcount=[]
x=[]
time=[]
Ttime=[]
time2=[]
rnk=[]
rnk2=[]
rat=[]
p=0
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    i=1
    k=0
    for row in results:
        i=i+1
        Rt= row[0]
        Ft = row[1]
        diff=row[2]
        rank=row[3]
        #if int(diff)<864000 and int(Rt+Ft) >7200:
           # p=p+1
        #time.insert(i,int(diff)/60)
        #count.insert(i,(Ft+Rt))
        #if rank<0:
           # rank=0
        tem=(1.01*math.log(Ft+2*Rt)-(float(diff)/692800)-1.1*math.log(float(1.1-math.exp(-1*float(diff)/692800))))
       # print(math.log(float(1.001-math.exp(-1*float(diff)/2300))))
        #tem=(10000*math.log(Ft+2*Rt)-50*(float(diff)/2300))
        #tem=(math.log(Ft+2*Rt)-math.log(float(1.001-math.exp(-1*float(diff)/355))))
        #tem=(math.log(Ft+2*Rt)-(float(diff)/35590))
        '''
        if rank> 7.5:
            #print(math.exp(-1*float(diff)/3559))

            k=k+1
            time.append(int(diff)/3600)
            count.append((Ft+2*Rt))
            x.append(i)
            rat.append(int(((Ft+2*Rt)*3600)/int(diff)))
            rnk.append(rank)
         '''
        #if (Ft+Rt)>1000:
            #Ttime.insert(k,int(diff))
            #Tcount.insert(k,(Ft+2*Rt))
        if tem>11.2:

            time.insert(k,int(diff))
            time2.insert(k,int(diff)/(60*60*24))
            #time.append(int(diff))
            #count.append((Ft+2*Rt))
            count.insert(k,(Ft+2*Rt))
            rnk2.insert(k,tem)
            k=k+1
           # x.append(i)
            #rat.append(int(((Ft+2*Rt))/int(diff)))
            #rnk2.append(math.exp(math.log(Ft+2*Rt)-(float(diff)/3559)-math.log(float(1.001-math.exp(-1*float(diff)/3559)))))





except:
    print ("Error: unable to fecth data")
#print(len(count))
#print(len(time))
#print(len(rnk2))
#print(len(results))

#print(i)
#print(p)
#a = np.array(count)
#u, count2 = np.unique(a,  return_counts=True)
#print(u.tolist())
#print(count2.tolist())
with open('Tweet.csv', 'w') as csvfile:
    fieldnames = ['Rank','RTweet_Fvrt','Life_time(days)','Life_time(Secs)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    j=0
    for row in rnk2:
        tem=float(float(time[j])/(60*60*24))
        writer.writerow({'Rank': rnk2[j], 'RTweet_Fvrt': count[j], 'Life_time(days)': tem, 'Life_time(Secs)': time[j]})
        j=j+1
'''
with open('TweetDataSetd.csv', 'w') as csvfile:
    fieldnames = ['RTweet_Fvrt','Life_time(days)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    j=0
    for row in Tcount:
        tem=float(float(Ttime[j])/(60*60*24))
        writer.writerow({ 'RTweet_Fvrt': Tcount[j], 'Life_time(days)': tem})
        j=j+1
'''

print("retweet count:",count)
print("life time (hours):",time2)
print("life time (hours):",time)
#print("rank:",rnk)
print("rank2:",rnk2)
print(k)
#print('rate:',rat)
#1=u.tolist()
#y= count2.tolist()
#plt.plot([0,10000],[3,3],'r-')


#plt.axis([0.5, 1.1, 6.5, 9])


#plt.plot(x,rnk, 'go')
db.close()


'''
plt.ylabel('Rank')
plt.xlabel('Retweet+Favourite per hour ')
plt.title("Mean Retweet Count(total retweet/life time of tweet) vs Rank")
plt.axis([2000, 3000, 6, 10])
plt.plot(rat,rnk2, 'bo')

'''
'''

plt.ylabel('Rank')
plt.xlabel('Life Time of tweet (hours) ')
plt.title("Life Time of tweet (hours) vs Rank")
plt.axis([30000,80000, 10, 12])
plt.plot(time,rnk2, 'ro')


'''
plt.ylabel('Rank')
plt.xlabel('Retweet+Favourite count ')
plt.title("Retweet+Favourite count vs Rank")
plt.axis([10000,12500, 8, 12])
plt.plot(count,rnk2, 'bo')


#plt.plot([0,7200],[14400,0],'r')
#plt.plot(count,time, 'go')

#print(len(y))
#print(np.std(y))
#print(np.mean(y))
#print(np.mean(x1))
#s=0
#for k in count2:
    #s=s+k
#print(s/13400)

#plt.plot(x, count, 'g')

plt.show()
#plt2.show()

