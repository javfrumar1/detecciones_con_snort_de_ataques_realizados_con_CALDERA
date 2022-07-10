import os
lines = []
alerts = []
with open('alerts') as f:
    lines = f.readlines()
for line in lines:
	if "[**]" in line:
		var = line.split(":")[1]
		if var not in alerts:
			alerts.append(var)

str_alertas = ""
for i in alerts:
	print(i)
	os.system('cat /etc/snort/rules/* | grep "sid:' + i + ';"') 
	if i != alerts[len(alerts)-1]:
		str_alertas += (i+",")
	else:
		str_alertas += i

print(str_alertas)
