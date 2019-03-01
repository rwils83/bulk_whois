import subprocess

ipsToCheck= ['google.com', '8.8.8.8']


for i in ipsToCheck:
 ip=i
 process = subprocess.Popen("whois %s | egrep '(NetRange|OrgTechName)' >> trial.text" %ip,
                             shell=True,
                             stdout=subprocess.PIPE,
                           )
 stdout_list = process.communicate()[0].split('\n')
 print stdout_list
 print '\n'


