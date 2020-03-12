import re



file = open("sample.txt")
file2 = open("featuresample.txt")
file3 = open("awesome.feature","w+")
data1=file2.readlines()

data = file.readlines()
dbcheck = re.match('db:*', data[0])
usercheck = re.match('user:*', data[1])
pswdcheck = re.match('pswd:*', data[2])
if(dbcheck and len(data[0])>3):
    db=data[0].replace('db:','')
    print(db)
else:
    print("Database details has not been provided")
if(usercheck and len(data[1])>5):
    user=data[1].replace('user:','')
    print(user)
else:
    print("Database details has not been provided")
if(pswdcheck and len(data[2])>5):
    pswd=data[2].replace('pswd:','')
    print(pswd)
else:
    print("Database details has not been provided")

for j in data1:
    print(j)
    if(re.match('\$db',j)):
        file3.write(j.replace('$db',(db)))
        continue
    elif (j.find('$user')):
        file3.write(j.replace('$user', (user)))
        print(j)
        continue
    elif (j.find('$pswd')):
        file3.write(j.replace('$pswd', 'abcd'))
        print(j)
        continue
    else:
        print("nope")
        continue
file.close()
file2.close()
file3.close()

