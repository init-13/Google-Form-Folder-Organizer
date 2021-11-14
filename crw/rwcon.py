import json

def write2config(dirl,fC,sep,fiC,fiN):

	data={ "folderC" : fC,"sep" : sep,"filesC": fiC,"filesN": fiN}
	with open(dirl+'/config.json','w') as file:
		json.dump(data,file)


