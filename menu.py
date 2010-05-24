import os
import random
from smtplib import *
import time
import pdb
import sqlite3
from LongestCommonSubStr import *


pwd = os.path.join(os.getcwd(), "menu2.txt")
file = open(pwd, 'r')
dbfile = os.path.join(os.getcwd(), "menu")

#conn = sqlite3.connect(dbfile)
#c = conn.cursor()
outStr = "we will eat this :\n"
ISOTIMEFORMAT='%Y-%m-%d %X'



dict = {}
list = []
#targets = ["yangjiandong@snda.com", "lijian01@snda.com", "gaoyong01@snda.com", "v.huangcheng01@snda.com",
#		"lichencheng@snda.com", "chensiru@snda.com", "v.yangjiamin@snda.com", "v.zhaojiajia@snda.com",
#            "sujiqiang@snda.com", "sunning@snda.com"]
#targets = ["yangjiandong@snda.com","sunning@snda.com"]
#define this:
meat = 6
veg = 2
n = 59
m = 80
sum = 0

ltmp = time.localtime()
aDate = time.strftime(ISOTIMEFORMAT, time.localtime())

if ltmp[3] < 13:
    aTime = 'lunch'
else:
    aTime = 'dinner'



while True:
    line = file.readline()
    if line:
        if (line != '\n'):
            (name, price) = line.split()
            dict[name] = int(price)
            list.append(name)
            #print name
    else:
        #print 'hell'
        break
file.close()

outStr += '\nmeat is: \n'
#print '\nmeat: '
lmenu = [' ']
flag = True

#pdb.set_trace()

i = 0
while i < meat:
    flag = True
    ran = random.randint(0, n)
    for sName in lmenu:
        (max, min) = rangeLen(sName, list[ran])
        aStr = lcs(max, min)
        if (len(aStr) > 3):
            flag = False
    if flag == True:
        i = i + 1
        sum += dict[list[ran]]
        outStr += list[ran]
        outStr += '\n'
        lmenu.append(list[ran])
    list[ran] = list[n]
    --n
#print '\nvebetables is : '
outStr += '\nvegetables is : \n'
i = 0
while i < veg:
    flag = True
    ran = random.randint(n+1, m)
    for sName in lmenu:
        (max, min) = rangeLen(sName, list[ran])
        aStr = lcs(max, min)
        if (len(aStr) > 3):
            flag = False
    if flag == True:
        i = i + 1
        sum += dict[list[ran]]
        outStr += list[ran]
        outStr += '\n'
        lmenu.append(list[ran])
    list[ran] = list[m]
    --m
   # print dict        
#print 'the total money is : %d\n' % sum
#tmp = (unicode(aDate), unicode(aTime), unicode(outStr), sum)
#c.execute('insert into menu values (?,?,?,?)', tmp)
#conn.commit()
#c.close()

outStr += 'the total money is : %d\n' % sum
outStr += '\n'
print outStr

head = 'Subject: menu order\nContent-Type: text/plain; charset=UTF-8\n\n\r'
mailcontent = (head + outStr + '%s ' % (time.asctime(),))



#smtp = SMTP("61.172.242.25")
#smtp.sendmail("yangjiandong@sdo.com", targets, mailcontent)
#smtp.quit()
#print "mail sent @ %s." % time.asctime()