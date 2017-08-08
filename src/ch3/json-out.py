import json
price = {
	"date" : "2017-11-11",
	"price" : {
		"Apple" : 80,
		"Strawberry" : 100,
		"Banana" : 30,
	}}
s = json.dumps(price)
print(s)
