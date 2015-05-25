'''
Python Class example
Testing the scope of variables
'''

class FirstClass():
	data = "spam"

	def __init__(self,value):
		self.data = value

	def display(self):
		print "Instance = ", self.data, "\t Class = ", FirstClass.data


def main():
	x = FirstClass("abc")
	y = FirstClass("31.8")

	print "x:"
	x.display()
	
	print "y:"
	y.display()


if __name__=="__main__":
	main()
