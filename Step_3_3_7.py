import requests, re

A = input()

site =requests.get(A).text

link = re.findall("href=[\"\'](.*?)[\"\']", site)
for a in link:
    print(a)