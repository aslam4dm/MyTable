#coded by jumb0
from col import colours as C
#apologies for the ugliness of my code! ¬.¬

# main class
class Table(object):

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

	def title(self, t):
		print("-"*self.column + "[", t, "]" + "-"*self.column)

	def style1(self):
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "-"*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}+".format(C.darkgrey) + "-"*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}+".format(C.darkgrey))
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
					print("{}| {}".format(C.darkgrey, C.end), "{}{}.{} {}{}{}".format(C.lightgrey, counter+1, C.end, C.red, i, C.end), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
				else:
					print("{}|{} {}{}.{} {}{}{}".format(C.darkgrey, C.end, C.lightgrey, counter+1, C.end, C.red, i, C.end), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
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
				#done don't change!
				print("{}|{}".format(C.darkgrey, C.end), " "*(6+self.Max_Length),  "{}|{}".format(C.darkgrey, C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "-"*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}+".format(C.darkgrey) + "-"*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}+{}".format(C.darkgrey, C.end))

	def style2(self):
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "="*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}+".format(C.darkgrey) + "="*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}+{}".format(C.darkgrey, C.end))
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
					print("{}| {}".format(C.darkgrey, C.end), "{}{}{}. {}{}{}".format(C.lightgrey, counter+1, C.end, C.red, i, C.end), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
				else:
					print("{}| {}{}{}.{} {}{}{}".format(C.darkgrey, C.end, C.lightgrey, counter+1, C.end, C.red, i, C.end), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
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
				#done don't change!
				print("{}|{}".format(C.darkgrey, C.end), " "*(6+self.Max_Length),  "{}|{}".format(C.darkgrey, C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "="*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}+".format(C.darkgrey) + "="*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}+{}".format(C.darkgrey, C.end))


	def style3(self):
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "~"*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}+".format(C.darkgrey) + "~"*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}+{}".format(C.darkgrey, C.end))
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
					print("{}| {}".format(C.darkgrey, C.end), "{}{}{}. {}{}{}".format(C.lightgrey, C.end, counter+1, C.red, i, C.end), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
				else:
					print("{}|{} {}{}.{} {}{}{}".format(C.darkgrey, C.end, C.lightgrey, C.end, counter+1, C.red, i, C.end), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
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
				#done don't change!
				print("{}|{}".format(C.darkgrey, C.end), " "*(6+self.Max_Length),  "{}|{}".format(C.darkgrey, C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "~"*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("+{}".format(C.darkgrey) + "~"*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}+{}".format(C.darkgrey, C.end))


	def style4(self):
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + ">"*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}X".format(C.darkgrey) + ">"*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}X{}".format(C.darkgrey, C.end))
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
					print("{}| {}".format(C.darkgrey, C.end), "{}{}{}. {}{}{}".format(C.lightgrey, counter+1, C.end, C.red, i, C.end), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
				else:
					print("{}|{} {}{}.{} {}{}".format(C.darkgrey, C.end, C.lightgrey, counter, C.end, C.red, i, C.end), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
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
				#done don't change!
				print("{}|{}".format(C.darkgrey, C.end), " "*(6+self.Max_Length),  "{}|{}".format(C.darkgrey, C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "<"*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}X".format(C.darkgrey) + "<"*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}X{}".format(C.darkgrey, C.end))


	def style5(self):
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "$"*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}$".format(C.darkgrey) + "$"*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}${}".format(C.darkgrey, C.end))
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
					print("{}${} ".format(C.darkgrey, C.end), "{}{}.{} {}{}{}".format(C.lightgrey, counter+1, C.end, C.red, i, C.end), " "*self.addon, "{}${}".format(C.darkgrey, C.end), end="",)
				else:
					print("{}${} {}{}.{} {}{}{}".format(C.darkgrey, C.end, C.lightgrey, counter+1, C.end, C.red, i, C.end), " "*self.addon, "{}${}".format(C.darkgrey, C.end), end="",)
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
				#done don't change!
				print("{}${}".format(C.darkgrey, C.end), " "*(6+self.Max_Length),  "{}${}".format(C.darkgrey, C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "$"*(6+self.Max_Length+3)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}$".format(C.darkgrey) + "$"*(6+self.Max_Length+3+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}${}".format(C.darkgrey, C.end))


# [  non numbered styles ]
# default char value of 4, && equal spaces
# with non numbered styles, the list index doesn't matter
# because number spaces are disregarded, thus each element
# prints with 2 whitespace, see line 18 in style6

	def style6(self):
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "~"*(4+self.Max_Length+2)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}+".format(C.darkgrey) + "~"*(4+self.Max_Length+2+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}+".format(C.darkgrey))
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
				print("{}|{}  {}{}".format(C.darkgrey, C.end, C.red, i), " "*self.addon, "{}|{}".format(C.darkgrey, C.end), end="",)
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
				#done don't change!
				print("{}|".format(C.darkgrey), " "*(3+self.Max_Length),  "{}|".format(C.darkgrey), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "~"*(4+self.Max_Length+2)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}+".format(C.darkgrey) + "~"*(4+self.Max_Length+2+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}+{}".format(C.darkgrey, C.end))


	def style7(self):
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "."*(4+self.Max_Length+2)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}o".format(C.darkgrey) + "."*(4+self.Max_Length+2+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}o{}".format(C.darkgrey, C.end))
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
				print("{}o{}  {}{}{}".format(C.darkgrey, C.end, C.red, i, C.end), " "*self.addon, "{}o{}".format(C.darkgrey, C.end), end="",)
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
				#done don't change!
				print("{}o".format(C.darkgrey), " "*(3+self.Max_Length),  "o{}".format(C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(C.darkgrey) + "."*(4+self.Max_Length+2)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}o".format(C.darkgrey) + "."*(4+self.Max_Length+2+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}o{}".format(C.darkgrey, C.end))


# with colour, requires 2 arguments
# arg1 = border colour; arg2 = text colour
	def style8(self, *args):
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(args[0]) + ">"*(4+self.Max_Length+2)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}%".format(args[0]) + ">"*(4+self.Max_Length+2+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}%{}".format(args[0], C.end))
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
				print("{}%{}  {}{}{}".format(args[0], C.end, args[1], i, C.end), " "*self.addon, "{}%{}".format(args[0], C.end), end="",)
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
				#done don't change!
				print("{}%".format(args[0]), " "*(3+self.Max_Length),  "%{}".format(C.end), end="")
		print("")
		for n in range(self.column):
			if (n > 0) and (n < self.column):
				print("{}".format(args[0]) + "<"*(4+self.Max_Length+2)+ "{}".format(C.end), end="",)
			elif (n == 0 or n+1 == self.column):
				print("{}%".format(args[0]) + "<"*(4+self.Max_Length+2+(self.column-2))+ "{}".format(C.end), end="",)
		print("{}%{}".format(args[0], C.end))
