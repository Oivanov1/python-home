infile = open("sample.log","r")
iplist = {}

for line in infile:
    line = line.strip()
    if line: 
        iplist.setdefault(line, 0) 
        iplist[line] += 1 

outfile = open("out.txt","w") 
for key in iplist.keys():
    if iplist[key]>10:
        line = "%-15s = %s" % (key, iplist[key])
        print (line)
        outfile.write(line + "\n")
