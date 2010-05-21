import os
import random
from smtplib import *
import time


pwd = os.path.join(os.getcwd(), "menu2.txt")
file = open(pwd, 'r')
outStr = "we will eat this :\n"


dict = {}
list = []
targets = ["yangjiandong@snda.com", "lijian01@snda.com", "gaoyong01@snda.com", "v.huangcheng01@snda.com",
		"lichencheng@snda.com", "chensiru@snda.com", "v.yangjiamin@snda.com", "v.zhaojiajia@snda.com",
            "sujiqiang@snda.com", "sunning@snda.com"]
#targets = ["yangjiandong@snda.com","sunning@snda.com"]
#define this:
meat = 6
veg = 2
n = 59
m = 80
sum = 0

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

for i in range(meat):
    ran = random.randint(0, n)
    sum += dict[list[ran]]
   # print list[ran]
    outStr += list[ran]
    outStr += '\n'
    list[ran] = list[n]
    --n
#print '\nvebetables is : '
outStr += '\nvegetables is : \n'
for i in range(veg):
    ran = random.randint(n+1, m)
    sum += dict[list[ran]]
#    print list[ran]
    outStr += list[ran]
    outStr += '\n'
    list[ran] = list[m]
    --m
   # print dict        
#print 'the total money is : %d\n' % sum
outStr += 'the total money is : %d\n' % sum
outStr += '\n'
print outStr
head = 'Subject: menu order\nContent-Type: text/plain; charset=UTF-8\n\n\r'
mailcontent = (head + outStr + '%s ' % (time.asctime(),))

smtp = SMTP("61.172.242.25")
smtp.sendmail("yangjiandong@sdo.com", targets, mailcontent)
smtp.quit()
print "mail sent @ %s." % time.asctime()