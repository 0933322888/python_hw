import os
import argparse
import re

parser = argparse.ArgumentParser(description="Finds 10 most common ip addresses in log")
parser.add_argument('path', help='path to log file')
args = parser.parse_args()
all_ips = {}
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with open(args.path) as file:
    lines = file.read()
    ips=re.findall(pattern, lines)
    
# create dict with ips and occurances
for ip in ips:
    if all_ips.get(ip) :
        current = all_ips[ip]
        all_ips[ip] = current + 1
    else :
        all_ips[ip] = 1

# sort dict by ip occurances
sorted_ips = {k: v for k, v in sorted(all_ips.items(), key=lambda item: item[1], reverse=True)}
keys = list(sorted_ips.keys())

for x in range(10):
    print(str(keys[x]) + " " + str(sorted_ips[keys[x]]))
