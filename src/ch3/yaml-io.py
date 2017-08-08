import yaml

champion = [
{ "name": "Teemo", "age": "5", "gender": "man" },
{ "name": "Vayne", "age": "15", "gender": "woman" },
{ "name": "Moondo", "age": "12", "gender": "man" },
{ "name": "Ezreal", "age": "20", "gender": "man" }
]

yaml_str = yaml.dump(champion)
print(yaml_str)
print("----- ----- -----\n")

data = yaml.load(yaml_str)

for p in data:
	print(p["name"])
