# coded by jumb0
from col import colours as C

# within numberless method, self.defaultSpacing should be 3
# new objective: find logical errors
# think about adding append option, for appending to a list while a list table has already been created

class Table(object):
	"""
	Create your own styled tables, numbered for menus, or non-numbered possibly for general information
	Instantiation is as follows:
	You could do T = MyTable.Table(["any", "list", "data", "..."], 2)
	T.make_table()	or T.numberless_table() which will provide you with the default set table & colours
				---OR (for customization of tables/menus)---
	T = MyTable.Table(["any", "list", "data", "..."], 2) # pass in a list of data; and specify the number of prefered columns
	T.title("Example of Use")		# title, style and colour methods are optional, each require some argument input
	T.style("|", "=", "#")			# first=verical border, second=horizontal, third[optional]=edges
	T.colour("\033[1;31m", "\033[0;32m")	# an easier option for colour is to import col, for ease
	T.make_table()	or T.numberless_table() # either of these will print your table to screen
	"""

	def __init__(self, data, column):
		self.column = column
		self.data = data
		self.Max_Length = 0
		for item in self.data:
			if len(item) > self.Max_Length:
				self.Max_Length = len(item)
		self.addon = None
		self.row = 0
		if self.column == 1:
			self.row = len(self.data)
		else:
			for i in range(len(self.data)):
				if i % self.column == 0:
					self.row += 1
			#colour and styling variables
		self.borders = C.darkgrey; self.text = C.cyan
		self.defaultStyle = ["|", "-", "+"]
		self.defaultSpacing = 6
		self.number_colour = C.lightgrey

	def title(self, t):
		print("-"*self.column + "[", t.upper(), "]" + "-"*self.column)

	def colour(self, **kwargs):
		"""
		keyword arguments include: border | text | number
		you should assign a colour to the specified keyword arg, e.g:
		example.colour(borders="\033[0;31m"...)
		example.colour(number="colour goes here", text="colour goes here")
		-> arguments needn't be ordered, nor do they have to all be selected
		together. Each argument could be processed individually.
		"""
		if len(kwargs)==1:
			try:
				self.borders = kwargs["border"]
				return(None)
			except: pass
			try:
				self.text = kwargs["text"]
				return(None)
			except: pass
			try:
				self.number_colour = kwargs["number"]
				return(None)
			except: pass
		elif len(kwargs)==2:
			try:
				self.borders = kwargs["border"]
				self.text = kwargs["text"]
				return(None)
			except: pass
			try:
				self.borders = kwargs["border"]
				self.number_colour = kwargs["number"]
				return(None)
			except: pass
			try: 
				self.text = kwargs["text"]
				self.number_colour = kwargs["number"]
				return(None)
			except: pass
		elif len(kwargs)==3:
			try:
				self.borders = kwargs["border"]
				self.text = kwargs["text"]
				self.number_colour = kwargs["number"]
				return(None)
			except: pass
		else:
			self.borders = C.blue
			self.text = C.orange
			self.number_colour = C.green  # possibly add randomly selected colouring if args not specified?

	def style(self, *args):
		"""
		the arguments to this method should include the vertical character, horizontal character and edges (optional)
		an example of how to create a stylish table may follow through as:
		example = MyTable.Table(["a","b"], 2)
		example.style("|", "=", "/"); example.numberless_table()
		in which case would look (something) like: 	/============/
					       			|  a  ||  b  |
					       			/============/
		it must be vertical first, and then horizontal second, with edges as optional third					       
		"""
		if len(args) > 2:
			self.defaultStyle = [args[0], args[1], args[2]]
		else:
			self.defaultStyle = [args[0], args[1], "+"]

	def make_table(self):
		self.defaultSpacing = 6
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(self.borders) + self.defaultStyle[1]*(self.defaultSpacing+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}{}".format(self.borders, self.defaultStyle[2]) + self.defaultStyle[1]*(self.defaultSpacing+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}{}{}".format(self.borders, self.defaultStyle[2], C.end))
		pipelines = 0
		counter = 0
		counter2 = 1
		for i in self.data:
			self.addon = 1
			try:
				while len(i)+self.addon != self.Max_Length+1: 
					self.addon += 1
					continue
				if counter % self.column == 0 and counter > 0:
					print("")
				if counter+1 < 10:
					print("{}{}{} ".format(self.borders, self.defaultStyle[0], C.end), "{}{}.{} {}{}{}".format(self.number_colour, counter+1, C.end, self.text, i, C.end), " "*self.addon, "{}{}{}".format(self.borders, self.defaultStyle[0], C.end), end="",)
				else:
					print("{}{}{} {}{}.{} {}{}{}".format(self.borders, self.defaultStyle[0], C.end, self.number_colour, counter+1, C.end, self.text, i, C.end), " "*self.addon, "{}{}{}".format(self.borders, self.defaultStyle[0], C.end), end="",)
				pipelines+=2
			except:
				pass
			counter += 1; counter2 += 1
		if len(self.data) % self.column != 0:
			c = self.column 	#column
			R = self.row		# row
			P = R*2				# num of pipelines
			oP = P*c 			# overall pipelines (that should exist)
			r = oP - pipelines 	# num of remainder (pipelines missing)
			for i in range(r//2):
				print("{}{}".format(self.borders, self.defaultStyle[0]), " "*(self.defaultSpacing+self.Max_Length),  "{}{}".format(self.defaultStyle[0], C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(self.borders) + self.defaultStyle[1]*(self.defaultSpacing+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}{}".format(self.borders, self.defaultStyle[2]) + self.defaultStyle[1]*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}{}{}".format(self.borders, self.defaultStyle[2], C.end))


	def numberless_table(self):
		self.defaultSpacing = 3
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(self.borders) + self.defaultStyle[1]*(self.defaultSpacing+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}{}".format(self.borders, self.defaultStyle[2]) + self.defaultStyle[1]*(self.defaultSpacing+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}{}{}".format(self.borders, self.defaultStyle[2], C.end))
		pipelines = 0
		counter = 0
		counter2 = 1
		for i in self.data:
			self.addon = 1
			try:
				while len(i)+self.addon != self.Max_Length+1: 
					self.addon += 1
					continue
				if counter % self.column == 0 and counter > 0:
					print("")
				if counter+1 < 10:
					print("{}{}{} ".format(self.borders, self.defaultStyle[0], C.end), "{}{}{}".format(self.text, i, C.end), " "*self.addon, "{}{}{}".format(self.borders, self.defaultStyle[0], C.end), end="",)
				else:
					print("{}{}{}  {}{}{}".format(self.borders, self.defaultStyle[0], C.end, self.text, i, C.end), " "*self.addon, "{}{}{}".format(self.borders, self.defaultStyle[0], C.end), end="",)
				pipelines+=2
			except:
				pass
			counter += 1; counter2 += 1
		if len(self.data) % self.column != 0:
			c = self.column 	
			R = self.row		
			P = R*2				
			oP = P*c 			
			r = oP - pipelines 	
			for i in range(r//2):
				print("{}{}".format(self.borders, self.defaultStyle[0]), " "*(self.defaultSpacing+self.Max_Length),  "{}{}".format(self.defaultStyle[0], C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(self.borders) + self.defaultStyle[1]*(self.defaultSpacing+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}{}".format(self.borders, self.defaultStyle[2]) + self.defaultStyle[1]*(self.defaultSpacing+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}{}{}".format(self.borders, self.defaultStyle[2], C.end))
