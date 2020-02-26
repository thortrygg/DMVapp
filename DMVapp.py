import pickle
import dmb_record

"""dmvcarrecord Class"""
class dmvcarrecord:
	def __init__(self, plate, make, model, year, owner, reg_expiry):
		self.plate = plate
		self.make = make
		self.model = model
		self.year = year
		self.owner = owner
		self.reg_expiry = reg_expiry


	def __str__(self):
		string =  'License #: ' + self.plate.title() + '\n'
		string = string + 'Year: ' + str(self.year) + '\n'
		string = string + 'Make: ' + str(self.make) + '\n' 
		string = string + 'Model: ' + str(self.model) + '\n'
		string = string + 'Owner: ' + str(self.owner) + '\n'
		string = string + 'Reg Expiration: ' + str(self.reg_expiry) + '\n'
		return string

"""Creating an empty list called DMVdatabase"""
DMVdatabase = []


print ('*********** DMV CAR RECORDS ***********\n')

"""Printing vehicle List one at a time"""
counter = 1
for x in DMVdatabase:
	print(f'Car# {counter}\n')
	print (DMVdatabase[counter-1])
	counter = counter+ 1


"""adding a new car to the list based on input"""
carrecord = dmvcarrecord (input('Enter Plate #: '),input('Enter Vehicle Make: '),input('Enter Vehicle Model: '), input('Enter Vehicle Year: '), input('Enter Owner Name: '), input('Registration Expiration: '))
DMVdatabase.append (carrecord) 

print ('*********** DMVdatabase List ***********\n')

"""Printing car List one at a time"""
counter = 1
for x in DMVdatabase:
	print(f'Car# {counter}\n')
	print (DMVdatabase[counter-1])
	counter = counter+ 1
	
"""Saving the List to a file using Pickle"""
filename = input('Enter a filename to save Carrecord: ')
with open(filename, 'wb') as outfile:
	pickle.dump(DMVdatabase, outfile)
print (f'****** Saving Car Record List to {filename} *******\n')	

"""Make the list empty and print it again"""
DMVdatabase = []
print ('*********** DMVdatabase List ***********\n')

"""Printing Car List one at a time"""
counter = 1
for x in DMVdatabase:
	print(f'Car# {counter}\n')
	print (DMVdatabase[counter-1])
	counter = counter+ 1
	
"""Loading the List from a file using Pickle"""
filename = input('Enter a filename to load DMVdatabase: ')
with open(filename, 'rb') as infile:
	DMVdatabase = pickle.load(infile)
print (f'****** Saving Car Record List to {filename} *******\n')	

print ('*********** DMVdatabase List ***********\n')

"""Printing car List one at a time"""
counter = 1
for x in DMVdatabase:
	print(f'Car# {counter}\n')
	print (DMVdatabase[counter-1])
	counter = counter+ 1
