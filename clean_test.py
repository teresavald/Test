from Tkinter import *
import time
import threading
import PIL
from PIL import Image
from PIL import ImageTk

class Application(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.stringVar_esn = StringVar() #Engine Serial Number
		self.stringVar_svn = StringVar() #Shop Visit Number
		self.stringVar_cpn = StringVar() #Combustor Part Number
		self.engineLine = ""
		self.combustor = ""
		self.group = ""
		self.esn = ""
		self.svn = ""
		self.cpn = ""
		self.parent_folder = ""
		self.dome_folder = ""
		self.inner_folder = ""
		self.outer_folder = ""
		self.manual_combustorGroup = 0
		self.cur_widgets = []
		self.value = 0
		self.createWidgets_EngineLine()
		

	def destroyWidgets(self):
		for child in self.winfo_children():
			child.destroy()
	
	def restart(self):
		print ("Llegue a restart")
		self.destroyWidgets()
		
		self.stringVar_esn = StringVar()
		self.stringVar_svn = StringVar()
		self.stringVar_cpn = StringVar()
		self.engineLine = ""
		self.combustor = ""
		self.group = ""
		self.esn = ""
		self.svn = ""
		self.cpn = ""
		self.parent_folder = ""
		self.dome_folder = ""
		self.inner_folder = ""
		self.outer_folder = ""
		self.value = 0
		self.createWidgets_EngineLine()
		
	def createWidgets_EngineLine(self):
		self.destroyWidgets()
		
		'''
		self.value = voltage_mean(0)
		print(self.value)
		'''

		self.manual_engine = 0
		self.engineLine = ""
		self.combustor = ""
		self.group = ""
		
		self.label_title = Label(self)
		self.label_title["text"] = "Engine Line?"
		self.label_title["font"] = ("bold", 30)
		#self.label_title["fg"] = "red"
		self.label_title.grid(row = 0, column = 0, columnspan = 3)
		
		self.label_blank = Label(self)
		self.label_blank["text"] = "."
		self.label_blank["height"] = 1

		self.label_blank["fg"] = "white"
		self.label_blank.grid(row = 1, column = 1)
		
		self.button_genx1b = Button(self)
		self.button_genx1b["text"] = "GEnx-1B"
		self.button_genx1b["font"] = 15
		self.button_genx1b["height"] = 4
		self.button_genx1b["width"] = 10
		self.button_genx1b["command"] = lambda: self.createWidgets_Combustor("GEnx-1B")
		self.button_genx1b.grid(row = 2, column = 0)
		
		self.button_genx2b = Button(self)
		self.button_genx2b["text"] = "GEnx-2B"
		self.button_genx2b["font"] = 15
		self.button_genx2b["height"] = 4
		self.button_genx2b["width"] = 10
		self.button_genx2b["command"] = lambda: self.createWidgets_Combustor("GEnx-2B")
		self.button_genx2b.grid(row = 2, column = 2)
		
		'''
		self.label_battery = Label(self)
		self.label_battery["text"] = "Battery: "
		self.label_battery["font"] = ("bold", 10)
		self.label_battery.grid(row = 0, column = 5)
		
		if self.value < 950: # Super low
			#call("sudo poweroff", shell=True)
			self.label_level = Label(self)
			self.label_level["text"] = "Super Low"
			self.label_level["font"] = 10
			self.label_level["fg"] = "Red"
			self.label_level.grid(row = 0, column = 6)
		elif self.value < 970: # Low Battery
			self.label_level = Label(self)
			self.label_level["text"] = "Low"
			self.label_level["font"] = 10
			self.label_level["fg"] = "Red"
			self.label_level.grid(row = 0, column = 6)
		elif self.value < 1000: # Medium Battery
			self.label_level = Label(self)
			self.label_level["text"] = "Medium"
			self.label_level["font"] = 10
			self.label_level["fg"] = "Yellow"
			self.label_level.grid(row = 0, column = 6)
		else:
			self.label_level = Label(self)
			self.label_level["text"] = "High"
			self.label_level["font"] = 10
			self.label_level["fg"] = "Green"
			self.label_level.grid(row = 0, column = 6)
		'''
		
	def createWidgets_Combustor(self, engine = ""):
		self.destroyWidgets()
		
		#self.value = voltage_mean(0)
		self.manual_combustorGroup = 0
		self.combustor = ""
		self.group = ""
		
		self.label_title = Label(self)
		self.label_title["text"] = "Combustor PN?"
		self.label_title["font"] = ("bold", 30)
		self.label_title.grid(row = 0, column = 0, columnspan = 3)
		
		if engine == "":
			self.createWidgets_Combustor(self.engineLine)
		else:
			if engine == "GEnx-1B":
				self.engineLine = "GEnx-1B"
				#Create Buttons
				
				self.label_blank = Label(self)
				self.label_blank["text"] = "."
				self.label_blank["height"] = 1
				self.label_blank["fg"] = "white"
				self.label_blank.grid(row = 1, column = 1)
				
				self.button_2258m80 = Button(self)
				self.button_2258m80["text"] = "2258M80"
				self.button_2258m80["font"] = 15
				self.button_2258m80["height"] = 4
				self.button_2258m80["width"] = 10
				self.button_2258m80["command"] = lambda: self.createWidgets_Group("2258M80")
				self.button_2258m80.grid(row = 2, column = 0)
				
				
				self.button_return = Button(self)
				self.button_return["text"] = "Return"
				self.button_return["font"] = 15
				self.button_return["height"] = 4
				self.button_return["width"] = 10
				self.button_return["wraplength"] = 60
				self.button_return["bg"] = "blue"
				self.button_return["fg"] = "white"
				self.button_return["command"] = self.createWidgets_EngineLine
				self.button_return.grid(row = 2, column = 2)
			elif engine == "GEnx-2B":
				self.engineLine = "GEnx-2B"
				
				self.label_blank = Label(self)
				self.label_blank["text"] = "."
				self.label_blank["height"] = 1
				self.label_blank["fg"] = "white"
				self.label_blank.grid(row = 1, column = 1)
				
				self.button_2258m80 = Button(self)
				self.button_2258m80["text"] = "2258M80"
				self.button_2258m80["font"] = 15
				self.button_2258m80["height"] = 4
				self.button_2258m80["width"] = 10
				self.button_2258m80["command"] = lambda: self.createWidgets_Group("2258M80")
				self.button_2258m80.grid(row = 2, column = 0)
				
				
				self.button_return = Button(self)
				self.button_return["text"] = "Return"
				self.button_return["font"] = 15
				self.button_return["height"] = 4
				self.button_return["width"] = 10
				self.button_return["wraplength"] = 60
				self.button_return["bg"] = "blue"
				self.button_return["fg"] = "white"
				self.button_return["command"] = self.createWidgets_EngineLine
				self.button_return.grid(row = 2, column = 2)
			else : # Here be dragons
				self.label_dragons = Label(self)
				self.label_dragons["text"] = "Here be Dragons!"
				self.label_dragons.grid(row = 2, column = 1)
				
				self.button_return = Button(self)
				self.button_return["text"] = "Return"
				self.button_return["font"] = 15
				self.button_return["height"] = 4
				self.button_return["width"] = 10
				self.button_return["wraplength"] = 60
				self.button_return["bg"] = "blue"
				self.button_return["fg"] = "white"
				self.button_return["command"] = self.createWidgets_EngineLine
				self.button_return.grid(row = 3, column = 2)
				
			'''	
			self.label_battery = Label(self)
			self.label_battery["text"] = "Battery: "
			self.label_battery["font"] = ("bold", 10)
			self.label_battery.grid(row = 0, column = 5)
			
			if self.value < 950: # Super low
				#call("sudo poweroff", shell=True)
				self.label_level = Label(self)
				self.label_level["text"] = "Super Low"
				self.label_level["font"] = 10
				self.label_level["fg"] = "Red"
				self.label_level.grid(row = 0, column = 6)
			elif self.value < 970: # Low Battery
				self.label_level = Label(self)
				self.label_level["text"] = "Low"
				self.label_level["font"] = 10
				self.label_level["fg"] = "Red"
				self.label_level.grid(row = 0, column = 6)
			elif self.value < 1000: # Medium Battery
				self.label_level = Label(self)
				self.label_level["text"] = "Medium"
				self.label_level["font"] = 10
				self.label_level["fg"] = "Yellow"
				self.label_level.grid(row = 0, column = 6)
			else:
				self.label_level = Label(self)
				self.label_level["text"] = "High"
				self.label_level["font"] = 10
				self.label_level["fg"] = "Green"
				self.label_level.grid(row = 0, column = 6)
			'''
				
		
	def createWidgets_Group(self, combustor = ""):
		self.destroyWidgets()
		
		#self.value = voltage_mean(0)
		
		self.group = ""
		
		self.combustor = ""
		self.group = ""
		
		self.label_title = Label(self)
		self.label_title["text"] = "Group?"
		self.label_title["font"] = ("bold", 30)
		self.label_title.grid(row = 0, column = 0, columnspan = 5)
		
		if combustor == "":
			self.createWidgets_Combustor(self.combustor)
		else:
			if combustor == "2258M80":
				self.combustor = "2258M80"
				
				if self.engineLine == "GEnx-1B":
					self.button_g01 = Button(self)
					self.button_g01["text"] = "G01"
					self.button_g01["font"] = 15
					self.button_g01["height"] = 4
					self.button_g01["width"] = 6
					self.button_g01["command"] = lambda: self.createWidgets_ManualInfo("G01")
					self.button_g01.grid(row = 2, column = 0)
					
					self.button_g04 = Button(self)
					self.button_g04["text"] = "G04"
					self.button_g04["font"] = 15
		
					self.button_g04["height"] = 4
					self.button_g04["width"] = 6
					self.button_g04["command"] = lambda: self.createWidgets_ManualInfo("G04")
					self.button_g04.grid(row = 2, column = 1)
					
					self.button_g06 = Button(self)
					self.button_g06["text"] = "G06"
					self.button_g06["font"] = 15
					self.button_g06["height"] = 4
					self.button_g06["width"] = 6
					self.button_g06["command"] = lambda: self.createWidgets_ManualInfo("G06")
					self.button_g06.grid(row = 2, column = 2)
					
					self.button_g07 = Button(self)
					self.button_g07["text"] = "G07"
					self.button_g07["font"] = 15
					self.button_g07["height"] = 4
					self.button_g07["width"] = 6
					self.button_g07["command"] = lambda: self.createWidgets_ManualInfo("G07")
					self.button_g07.grid(row = 2, column = 3)
					
					self.button_g08 = Button(self)
					self.button_g08["text"] = "G08"
					self.button_g08["font"] = 15
					self.button_g08["height"] = 4
					self.button_g08["width"] = 6
					self.button_g08["command"] = lambda: self.createWidgets_ManualInfo("G08")
					self.button_g08.grid(row = 2, column = 4)
					
					self.button_g09 = Button(self)
					self.button_g09["text"] = "G09"
					self.button_g09["font"] = 15
					self.button_g09["height"] = 4
					self.button_g09["width"] = 6
					self.button_g09["command"] = lambda: self.createWidgets_ManualInfo("G09")
					self.button_g09.grid(row = 3, column = 0)
					
					self.button_g10 = Button(self)
					self.button_g10["text"] = "G10"
					self.button_g10["font"] = 15
					self.button_g10["height"] = 4
					self.button_g10["width"] = 6
					self.button_g10["command"] = lambda: self.createWidgets_ManualInfo("G10")
					self.button_g10.grid(row = 3, column = 1)
					
					self.button_g13 = Button(self)
					self.button_g13["text"] = "G13"
					self.button_g13["font"] = 15
					self.button_g13["height"] = 4
					self.button_g13["width"] = 6
					self.button_g13["command"] = lambda: self.createWidgets_ManualInfo("G13")
					self.button_g13.grid(row = 3, column = 2)
					
					self.button_return = Button(self)
					self.button_return["text"] = "Return"
					self.button_return["font"] = 15
					self.button_return["height"] = 4
					self.button_return["width"] = 10
					self.button_return["wraplength"] = 60
					self.button_return["bg"] = "blue"
					self.button_return["fg"] = "white"
					self.button_return["command"] = lambda: self.createWidgets_Combustor(self.engineLine)
					self.button_return.grid(row = 3, column = 3, columnspan = 2)
					
					
				else:
					self.button_g01 = Button(self)
					self.button_g01["text"] = "G01"
					self.button_g01["font"] = 15
					self.button_g01["height"] = 4
					self.button_g01["width"] = 6
					self.button_g01["command"] = lambda: self.createWidgets_ManualInfo("G01")
					self.button_g01.grid(row = 2, column = 0)
					
					self.button_g04 = Button(self)
					self.button_g04["text"] = "G04"
					self.button_g04["font"] = 15
					self.button_g04["height"] = 4
					self.button_g04["width"] = 6
					self.button_g04["command"] = lambda: self.createWidgets_ManualInfo("G04")
					self.button_g04.grid(row = 2, column = 1)
					
					self.button_g07 = Button(self)
					self.button_g07["text"] = "G07"
					self.button_g07["font"] = 15
					self.button_g07["height"] = 4
					self.button_g07["width"] = 6
					self.button_g07["command"] = lambda: self.createWidgets_ManualInfo("G07")
					self.button_g07.grid(row = 2, column = 2)
					
					self.button_g09 = Button(self)
					self.button_g09["text"] = "G09"
					self.button_g09["font"] = 15
					self.button_g09["height"] = 4
					self.button_g09["width"] = 6
					self.button_g09["command"] = lambda: self.createWidgets_ManualInfo("G09")
					self.button_g09.grid(row = 2, column = 3)
					
					self.button_g12 = Button(self)
					self.button_g12["text"] = "G12"
					self.button_g12["font"] = 15
					self.button_g12["height"] = 4
					self.button_g12["width"] = 6
					self.button_g12["command"] = lambda: self.createWidgets_ManualInfo("G12")
					self.button_g12.grid(row = 3, column = 0)
					
					
					self.button_return = Button(self)
					self.button_return["text"] = "Return"
					self.button_return["font"] = 15
					self.button_return["height"] = 4
					self.button_return["width"] = 10
					self.button_return["wraplength"] = 60
					self.button_return["bg"] = "blue"
					self.button_return["fg"] = "white"
					self.button_return["command"] = lambda: self.createWidgets_Combustor(self.engineLine)
					self.button_return.grid(row = 3, column = 2, columnspan = 2)

			else : # Here be dragons
				self.label_dragons = Label(self)
				self.label_dragons["text"] = "Here be Dragons!"
				self.label_dragons.grid(row = 2, column = 1)
				
				self.button_return = Button(self)
				self.button_return["text"] = "Return"
				self.button_return["font"] = 15
				self.button_return["height"] = 4
				self.button_return["width"] = 10
				self.button_return["wraplength"] = 60
				self.button_return["bg"] = "blue"
				self.button_return["fg"] = "white"
				self.button_return["command"] = lambda: self.createWidgets_Combustor(self.combustor)
				self.button_return.grid(row = 3, column = 3)
				
			'''
			self.label_battery = Label(self)
			self.label_battery["text"] = "Battery: "
			self.label_battery["font"] = ("bold", 10)
			self.label_battery.grid(row = 0, column = 5)
			
			if self.value < 950: # Super low
				#call("sudo poweroff", shell=True)
				self.label_level = Label(self)
				self.label_level["text"] = "Super Low"
				self.label_level["font"] = 10
				self.label_level["fg"] = "Red"
				self.label_level.grid(row = 0, column = 6)
			elif self.value < 970: # Low Battery
				self.label_level = Label(self)
				self.label_level["text"] = "Low"
				self.label_level["font"] = 10
				self.label_level["fg"] = "Red"
				self.label_level.grid(row = 0, column = 6)
			elif self.value < 1000: # Medium Battery
				self.label_level = Label(self)
				self.label_level["text"] = "Medium"
				self.label_level["font"] = 10
				self.label_level["fg"] = "Yellow"
				self.label_level.grid(row = 0, column = 6)
			else:
				self.label_level = Label(self)
				self.label_level["text"] = "High"
				self.label_level["font"] = 10
				self.label_level["fg"] = "Green"
				self.label_level.grid(row = 0, column = 6)
			'''
	
	def createWidgets_ManualInfo(self, group = ""):
		self.destroyWidgets()
		self.group = group
		
		#self.value = voltage_mean(0)
		
		#Initialize pic servo
		#pic.Init()
		#time.sleep(1)
		#pic.SetGain(100, 1000, 0, 0, 255, 0, 4000, 1, 1)
		#time.sleep(1)
		#pic.ServoOn()
		
		#pic.Go(0, 1000, 100, 0)
			
		
		self.stringVar_esn.set(self.esn)
		self.stringVar_svn.set(self.svn)
		
		self.label_esn = Label(self)
		self.label_esn["text"] = "Engine Serial Number:"
		self.label_esn["font"] = 20
		self.label_esn.grid(row = 0, column = 0)
		
		self.label_svn = Label(self)
		self.label_svn["text"] = "Shop Visit Number:"
		self.label_svn["font"] = 20
		self.label_svn.grid(row = 1, column = 0)
		
		self.entry_esn = Entry(self)
		self.entry_esn["textvariable"] = self.stringVar_esn
		self.entry_esn.grid(row = 0, column = 1, columnspan = 2, ipady = 6)
		
		self.entry_svn = Entry(self)
		self.entry_svn["textvariable"] = self.stringVar_svn
		self.entry_svn.grid(row = 1, column = 1, columnspan = 2, ipady = 6)
				
		self.button_next = Button(self)
		self.button_next["text"] = "Go"
		self.button_next["font"] = 15
		self.button_next["height"] = 4
		self.button_next["width"] = 10
		self.button_next["wraplength"] = 60
		self.button_next["bg"] = "green"
		self.button_next["fg"] = "white"
		self.button_next["command"] = self.createWidgets_Finished
		self.button_next.grid(row = 4, column = 0)
		
		self.button_restart = Button(self)
		self.button_restart["text"] = "Restart"
		self.button_restart["font"] = 15
		self.button_restart["height"] = 4
		self.button_restart["width"] = 10
		self.button_restart["wraplength"] = 60
		self.button_restart["bg"] = "black"
		self.button_restart["fg"] = "white"
		self.button_restart["command"] = self.restart
		self.button_restart.grid(row = 4, column = 2)
		
		# Check
		# Engine Line
		self.label_engineLine = Label(self)
		self.label_engineLine["text"] = "Engine Line: " + self.engineLine
		self.label_engineLine["heigh"] = 1
		self.label_engineLine["fg"] = "black"
		self.label_engineLine.grid(row = 5, column = 0, columnspan = 2)
		
		# Combustor
		self.label_combustor = Label(self)
		self.label_combustor["text"] = "Combustor: " + self.combustor
		self.label_combustor["heigh"] = 1
		self.label_combustor["fg"] = "black"
		self.label_combustor.grid(row = 6, column = 0, columnspan = 2)
		
		# Group
		self.label_group = Label(self)
		self.label_group["text"] = "Group: " + self.group
		self.label_group["heigh"] = 1
		self.label_group["fg"] = "black"
		self.label_group.grid(row = 7, column = 0, columnspan = 2)
		
		self.label_message = Label(self)
		self.label_message["text"] = "Release the arm before pressing 'Go'"
		self.label_message["height"] = 2
		self.label_message["font"] = ("bold", 20)
		self.label_message["fg"] = "Red"
		self.label_message["bg"] = "Yellow"
		self.label_message.grid(row = 8, column = 0, columnspan = 5)

	def show_running(self):
		self.destroyWidgets()
		
		self.label_message = Label(self)
		self.label_message["text"] = "Running Process"
		self.label_message["height"] = 2
		self.label_message["font"] = ("bold", 20)
		self.label_message["fg"] = "black"
		self.label_message["bg"] = "white"
		self.label_message.grid(row = 8, column = 0, columnspan = 5)
		
		self.start_process()
		#self.send_routine()
				
	def send_routine(self):
		self.esn = self.stringVar_esn.get()
		self.svn = self.stringVar_svn.get()
		self.cpn = self.combustor
		
		for i in range(5):
			print i
			time.sleep(1)

		self.createWidgets_Finished()
		
	def start_process(self):
		self.thread = threading.Thread(target = self.send_routine)
		self.thread.start()
		
		#thread.start_new(self.send_routine, ())
		#thread.start_new(self.show_running, ())
		#self.send_routine()
		
	def createWidgets_Finished(self):
		print("Entre a createWidgets_Finished")
		self.destroyWidgets()
				
		#self.value = voltage_mean(0)
		
		#update_file(int(doms * 3))
		
		self.label_title = Label(self)
		self.label_title["text"] = "Finished!"
		self.label_title["font"] = ("bold", 40)
		self.label_title.grid(row = 0, column = 0, columnspan = 5)
		
		self.button_restart = Button(self)
		self.button_restart["text"] = "Restart"
		self.button_restart["font"] = 15
		self.button_restart["height"] = 4
		self.button_restart["width"] = 10
		self.button_restart["wraplength"] = 60
		self.button_restart["bg"] = "black"
		self.button_restart["fg"] = "white"
		self.button_restart["command"] = self.restart
		self.button_restart.grid(row = 3, column = 1)
		
		self.button_photos = Button(self)
		self.button_photos["text"] = "Photos"
		self.button_photos["font"] = 15
		self.button_photos["height"] = 4
		self.button_photos["width"] = 10
		self.button_photos["wraplength"] = 60
		self.button_photos["bg"] = "green"
		self.button_photos["fg"] = "black"
		self.button_photos["command"] = lambda:self.createWidgets_Photos(0, 0, 0)
		self.button_photos.grid(row = 3, column = 3)
	
	def createWidgets_Photos(self, part = 0, pos = 0, dom_num = 0): # Part 0 (Dome), 1 (Inner Liner), 2 (Outer Liner)
		self.destroyWidgets()
		
		global doms
		global img
		global pre_img
		
		#angle_doms = int(360 / doms)
		
		#position = pos
		
		# if position < 0 or position > 360:
			# position = 0
			
		# if dom_num == 0:
			# position = 0
			
		
		# if part == 0:
			# path = self.dome_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
			# part_name = "(Dome - position:  " + str(int(dom_num)) + ")"
			# if not os.path.isfile(path):
				# position = position + 1
				# path = self.dome_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
				# if not os.path.isfile(path):
					# position = position - 2
					# path = self.dome_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
		# elif part == 1:
			# path = self.inner_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
			# part_name = "(Inner Liner - position:  " + str(int(dom_num)) + ")"
			# if not os.path.isfile(path):
				# position = position + 1
				# path = self.inner_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
				# if not os.path.isfile(path):
					# position = position - 2
					# path = self.inner_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
		# else:
			# path = self.outer_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
			# part_name = "(Outer Liner - position:  " + str(int(dom_num)) + ")"
			# if not os.path.isfile(path):
				# position = position + 1
				# path = self.outer_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
				# if not os.path.isfile(path):
					# position = position - 2
					# path = self.outer_folder + "/" + self.cpn + "-" + str(int(position)) + ".jpg"
		
		# print(path)
		# print(part_name)	
		
		self.label_title = Label(self)
		self.label_title["text"] = "Image Viewer: " #+ part_name
		self.label_title["font"] = ("bold", 20)
		self.label_title.grid(row = 0, column = 0, columnspan = 6)
		
		
		size = 400, 300
		path = "./2258M80-000.jpg"
		
		pre_img = PIL.Image.open(path)
		pre_img.thumbnail(size, PIL.Image.ANTIALIAS)
		img = PIL.ImageTk.PhotoImage(pre_img)
		
		self.label_photo = Label(self, image = img)
		self.label_photo.grid(row = 1, column = 0, columnspan = 6, rowspan = 5)
		
		self.button_previous = Button(self)
		self.button_previous["text"] = "<--"
		self.button_previous["font"] = 15
		self.button_previous["height"] = 4
		self.button_previous["width"] = 8
		self.button_previous["wraplength"] = 60
		self.button_previous["bg"] = "green"
		self.button_previous["fg"] = "black"
		self.button_previous["command"] = lambda:self.createWidgets_Photos(part, int(position + 360 - angle_doms) % 360, int(dom_num + doms - 1) % int(doms))
		self.button_previous.grid(row = 6, column = 0)
		
		self.button_dome = Button(self)
		self.button_dome["text"] = "Dome"
		self.button_dome["font"] = 15
		self.button_dome["height"] = 4
		self.button_dome["width"] = 8
		self.button_dome["wraplength"] = 60
		self.button_dome["bg"] = "blue"
		self.button_dome["fg"] = "black"
		self.button_dome["command"] = lambda:self.createWidgets_Photos(0, 0, 0)
		self.button_dome.grid(row = 6, column = 1)
		
		self.button_inner = Button(self)
		self.button_inner["text"] = "Inner Line"
		self.button_inner["font"] = 15
		self.button_inner["height"] = 4
		self.button_inner["width"] = 8
		self.button_inner["wraplength"] = 60
		self.button_inner["bg"] = "blue"
		self.button_inner["fg"] = "black"
		self.button_inner["command"] = lambda:self.createWidgets_Photos(1, 0, 0)
		self.button_inner.grid(row = 6, column = 2)
		
		self.button_outer = Button(self)
		self.button_outer["text"] = "Outer Liner"
		self.button_outer["font"] = 15
		self.button_outer["height"] = 4
		self.button_outer["width"] = 8
		self.button_outer["wraplength"] = 60
		self.button_outer["bg"] = "blue"
		self.button_outer["fg"] = "black"
		self.button_outer["command"] = lambda:self.createWidgets_Photos(2, 0, 0)
		self.button_outer.grid(row = 6, column = 3)
		
		self.button_next = Button(self)
		self.button_next["text"] = "-->"
		self.button_next["font"] = 15
		self.button_next["height"] = 4
		self.button_next["width"] = 8
		self.button_next["wraplength"] = 60
		self.button_next["bg"] = "green"
		self.button_next["fg"] = "black"
		self.button_next["command"] = lambda:self.createWidgets_Photos(part, int(position + angle_doms) % 360, int(dom_num + 1) % int(doms))
		self.button_next.grid(row = 6, column = 4)
		
		self.button_restart = Button(self)
		self.button_restart["text"] = "Restart"
		self.button_restart["font"] = 15
		self.button_restart["height"] = 4
		self.button_restart["width"] = 8
		self.button_restart["wraplength"] = 60
		self.button_restart["bg"] = "black"
		self.button_restart["fg"] = "white"
		self.button_restart["command"] = self.restart
		self.button_restart.grid(row = 6, column = 5)
		
		self.button_restart = Button(self)
		self.button_restart["text"] = "Power-Off"
		self.button_restart["font"] = 15
		self.button_restart["height"] = 4
		self.button_restart["width"] = 8
		self.button_restart["wraplength"] = 60
		self.button_restart["bg"] = "red"
		self.button_restart["fg"] = "white"
		#self.button_restart["command"] = lambda:call("sudo poweroff", shell=True)
		self.button_restart.grid(row = 6, column = 6)
		
	def createWidgets_Error(self, type = 0):
		self.destroyWidgets()
		
		#self.value = voltage_mean(0)
		
		self.label_title = Label(self)
		self.label_title["text"] = "ERROR!!"
		self.label_title["font"] = ("bold", 40)
		self.label_title["bg"] = "Red"
		self.label_title["fg"] = "Black"
		self.label_title.grid(row = 0, column = 0, columnspan = 5)
		
		if type == 0:
			self.label_error_1 = Label(self)
			self.label_error_1["text"] = "Something is blocking the path of the arm."
			self.label_error_1["font"] = 20
			self.label_error_1["fg"] = "Red"
			self.label_error_1.grid(row = 1, column = 0, columnspan = 5)
			
			self.label_error_2 = Label(self)
			self.label_error_2["text"] = "Check it and restart the application. Press the emergency button before moving the arm."
			self.label_error_2["font"] = 20
			self.label_error_2["fg"] = "Red"
			self.label_error_2.grid(row = 2, column = 0, columnspan = 5)
			
			self.label_blank = Label(self)
			self.label_blank["text"] = "."
			self.label_blank["height"] = 1
			self.label_blank["fg"] = "white"
			self.label_blank.grid(row = 3, column = 1)
		elif type == 1:
			self.label_error_1 = Label(self)
			self.label_error_1["text"] = "A communication error with the micro maestro occurred."
			self.label_error_1["font"] = 20
			self.label_error_1["fg"] = "Red"
			self.label_error_1.grid(row = 1, column = 0, columnspan = 5)
			
			self.label_error_2 = Label(self)
			self.label_error_2["text"] = "Check it and restart the application."
			self.label_error_2["font"] = 20
			self.label_error_2["fg"] = "Red"
			self.label_error_2.grid(row = 2, column = 0, columnspan = 5)
			
			self.label_blank = Label(self)
			self.label_blank["text"] = "."
			self.label_blank["height"] = 1
			self.label_blank["fg"] = "white"
			self.label_blank.grid(row = 3, column = 1)
		else:
			pass
		
		self.button_restart = Button(self)
		self.button_restart["text"] = "Restart"
		self.button_restart["font"] = 15
		self.button_restart["height"] = 4
		self.button_restart["width"] = 10
		self.button_restart["wraplength"] = 60
		self.button_restart["bg"] = "black"
		self.button_restart["fg"] = "white"
		self.button_restart["command"] = self.restart
		self.button_restart.grid(row = 4, column = 1)
		
		self.button_restart = Button(self)
		self.button_restart["text"] = "Back"
		self.button_restart["font"] = 15
		self.button_restart["height"] = 4
		self.button_restart["width"] = 10
		self.button_restart["wraplength"] = 60
		self.button_restart["bg"] = "green"
		self.button_restart["fg"] = "black"
		self.button_restart["command"] = lambda:self.createWidgets_ManualInfo(self.group)
		self.button_restart.grid(row = 4, column = 3)
		
		'''
		self.label_battery = Label(self)
		self.label_battery["text"] = "Battery: "
		self.label_battery["font"] = ("bold", 10)
		self.label_battery.grid(row = 0, column = 5)
		
		if self.value < 950: # Super low
			#call("sudo poweroff", shell=True)
			self.label_level = Label(self)
			self.label_level["text"] = "Super Low"
			self.label_level["font"] = 10
			self.label_level["fg"] = "Red"
			self.label_level.grid(row = 0, column = 6)
		elif self.value < 970: # Low Battery
			self.label_level = Label(self)
			self.label_level["text"] = "Low"
			self.label_level["font"] = 10
			self.label_level["fg"] = "Red"
			self.label_level.grid(row = 0, column = 6)
		elif self.value < 1000: # Medium Battery
			self.label_level = Label(self)
			self.label_level["text"] = "Medium"
			self.label_level["font"] = 10
			self.label_level["fg"] = "Yellow"
			self.label_level.grid(row = 0, column = 6)
		else:
			self.label_level = Label(self)
			self.label_level["text"] = "High"
			self.label_level["font"] = 10
			self.label_level["fg"] = "Green"
			self.label_level.grid(row = 0, column = 6)
		'''
		
root = Tk()
root.title("Robot Control")

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

w = ws/2  # width for the Tk root
h = hs/2  # height for the Tk root

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs) - (h)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

app = Application(master = root)
app.mainloop()