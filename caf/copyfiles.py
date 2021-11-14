import shutil

def copyall(dest_folder,csv_dest):
	shutil.copy(csv_dest,dest_folder)
	files = ['caf/Run.pyc', 'caf/config.json', 'caf/token_drive_v3.pickle','caf/cred.json']
	for f in files:
	    shutil.copy(f, dest_folder)

#copyall("C:/Users/Del/Desktop/GFO/caf/test","C:/Users/Del/Desktop/GFO/temp/Enrollment Data CS-A2L, 2020-21.csv")