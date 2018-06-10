from general import *

def lambda_handler(event, context):
	v1 = getJsonValue(event, "key1")
	v2 = getJsonValue(event, "key2")
	v3 = getJsonValue(event, "key3")
	v4 = getJsonValue(event, "key4")
	v5 = getJsonValue(event, "key5", "NA")

	print("Key1: {}".format(v1))
	print("Key2: {}".format(v2))
	print("Key3: {}".format(v3))
	print("Key4: {}".format(v4))
	print("Key5: {}".format(v5))

	return "Hello from Lambda"