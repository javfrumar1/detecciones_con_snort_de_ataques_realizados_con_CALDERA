import os
lines = []
alerts = []
with open('alert_fast.txt') as f:
    lines = f.readlines()
for line in lines:
	if "[**]" in line:
		var = line.split("[**]")[1].split(":")[1]
		if var not in alerts:
			alerts.append(var)

str_alertas = ""
for i in alerts:
    print("--> TALOS: "+ i)
    os.system('cat /usr/local/etc/rules/lightspd/rules/3.0.0.0/* | grep "sid:' + i + ';"')
    print("--> COMMUNITY: "+ i)
    os.system('cat /usr/local/etc/rules/snort3-community-rules/snort3-community.rules | grep "sid:' + i + ';"')
    print("\n")
    if i != alerts[len(alerts)-1]:
        str_alertas += (i+",")
    else:
        str_alertas += i
print(str_alertas)
