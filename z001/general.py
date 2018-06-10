def getJsonValue(pJson, pKey, pDefaultIfAbsent = ""):
	value = pJson.get(pKey, pDefaultIfAbsent)
	return value