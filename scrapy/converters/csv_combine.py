fout=open("000.csv","a")

# write first file:
for line in open('0.csv'):
    fout.write(line)

# now the second and next...:
for num in range(0,50):
    f = open(str(num)+'.csv')
    f.__next__() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()