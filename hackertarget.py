import requests
import argparse

parser = argparse.ArgumentParser(description='Map hackertarget domains -> ips for a list of domains')
parser.add_argument('--domain', type=str, help='The file that contains the hosts')
args = parser.parse_args()

domains = open(args.domain).read().split('\n')

for domain in domains:
    url = 'https://api.hackertarget.com/hostsearch/?q=' + domain
    request = requests.get(url).text

    for line in request.split('\n')[:-1]:
        fields = map(lambda s: s.strip(), line.split(','))
        print(fields[0] + " -> " + fields[1])
