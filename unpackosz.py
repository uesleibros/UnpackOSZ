import os
import zipfile
import shutil

def unpack(file, create_folder = True, prevent_file = True):
	if prevent_file:
		shutil.copy(file + ".osz", file + "_prevent.osz")
		file = file + "_prevent"
	oszFile = file + ".osz"
	zipFile = file + ".zip"
	folder = ""
	
	if os.path.exists(oszFile):
		os.rename(oszFile, zipFile)
		
		if create_folder:
			if not os.path.exists(file):
				print("Creating folder...")
				os.mkdir(file)
				
				folder = file
			else:
				folder = file
		
		print("Extracting files...")
		with zipfile.ZipFile(zipFile, "r") as zip:
			zip.extractall(folder)
			
		if prevent_file:
			os.rename(file, file.replace("_prevent", ""))
			os.remove(file + ".zip")
		else:
			os.remove(file + ".zip")
		
		print("Done!")
			
	return None
	
unpack("Example", True, True)