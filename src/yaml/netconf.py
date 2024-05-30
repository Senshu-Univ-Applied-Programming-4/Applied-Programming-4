import yaml

with open("netconf.yaml") as f:
	conf = yaml.safe_load(f)

print(conf)

print(conf['Server']['AllowIP'])
print(conf['Server']['Port'])
serverconf = conf['Server']
print(serverconf['AllowIP'])
print(serverconf['Port'])


print(conf['Client']['ServerIP'])
print(conf['Client']['ServerPort'])
clientconf = conf['Client']
print(clientconf['ServerIP'])
print(clientconf['ServerPort'])



