import os
from pathlib import Path

def output_dir(path, num_tabs):
	gap=""
	for i in range(num_tabs):
		gap+="  "
	size=0		
	for filename in os.listdir(path):
		full_path = path + "/" + filename
		if os.path.isdir(full_path):
			print (gap + "Directory: " + filename)
			size+=output_dir(full_path, num_tabs+1)
		elif os.path.isfile(full_path):
			size+=os.path.getsize(full_path)
			print (gap + "File: " + filename + " = " + str(os.path.getsize(full_path)))
		else:
			print(gap + "Other: " + filename)
	print(gap + "Size of directory: " + path + " = " + str(size))
	return size
	
path=input("What path do you want to start with?")
output_dir(path,0)
