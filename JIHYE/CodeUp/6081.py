n = input()
num16 = int(n,16)

for i in range(1,16) :
  print(n,"*",'%X'%i,"=",'%X'%(num16*i),sep='')
