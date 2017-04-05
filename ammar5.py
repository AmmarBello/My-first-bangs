print'Enter a file name'
res=raw_input()
file=open(res,'r+')
print"write some thing in {}".format(res)
wr=raw_input()
file.write(wr)
read=file.read()
print"Here is content of your file"
print''
print read
file.close()
