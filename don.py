print"What is your name"
name=raw_input(">>>")
print"what is your hobby"
answer=raw_input(">>>")
print"Can you recite?"
answer=raw_input(">>>")
try:
   answer=int(answer)
   if isinstance(answer, int):
       print "Hi "+name +" answer must be a letter"
except ValueError:
  print"Hi "+name +" answer must be a letter"
print"recite from baqarah to nass in your house"
try:
 answer=raw_input(">>>")
except ValueError:
  print"You are stupid"
print "What's your best number"
answer=raw_input(">>>" )







