import argparse

parser = argparse.ArgumentParser(description='Looking for top ips in log file.')
parser.add_argument("log_path", type=str, help='an path to log file')
args = parser.parse_args()
print (args)



infile = open(args.log_path,"r")
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
