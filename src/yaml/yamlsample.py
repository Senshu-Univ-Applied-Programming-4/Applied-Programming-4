import yaml

#yamlfiles=["set1.yaml","set2.yaml","set3.yaml","set4.yaml","set5.yaml","set6.yaml"]

yamlfiles=["set1.yaml"]

for filename in yamlfiles:
	with open(filename) as yamldat:
		conf = yaml.safe_load(yamldat)
	print(type(conf),conf)
