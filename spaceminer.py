import os

os.system("clear")

class File:

	def __init__(self, path, filename, size, num_tabs):
		self.path = path
		self.filename = filename
		self.size = size
		self.num_tabs = num_tabs
		
	def __str__(self):
		gap=""
		for i in range(self.num_tabs):
			gap+="  "
		return gap + self.filename + " - " + str(self.size)
		
	def print_me(self):
		gap=""
		for i in range(self.num_tabs):
			gap+="  "
		print(gap + self.filename + " - " + str(self.size))
		
	def print_out(self):
		self.print_me()
		
class Directory(File, object):
	def __init__(self, path, filename, size, num_tabs):
		super(Directory, self).__init__(path, filename, size, num_tabs)
		self.list_of_stuff=[]
	
	def addToStuff(self, thing):
		self.list_of_stuff+=[thing]
	
	def addToSize(self, size):
		self.size += size
		
	def print_out(self):
		self.print_me()
		for thing in self.list_of_stuff:
			thing.print_out()

def output_dir(directory, num_tabs):
	for filename in os.listdir(directory.path):
		full_path = directory.path + "/" + filename
		if os.path.isdir(full_path):
			new_dir = Directory(full_path, filename, 0, num_tabs)
			directory.addToStuff(new_dir)
			output_dir(new_dir, num_tabs+1)
			directory.addToSize(new_dir.size)
		elif os.path.isfile(full_path):
			file_size = os.path.getsize(full_path)
			new_file = File(full_path, filename,file_size, num_tabs)
			directory.addToStuff(new_file)
			directory.addToSize(file_size)
			
path=input("What path do you want to start with: ")
start_dir = Directory(path, path, 0, 0)
output_dir(start_dir,1)
