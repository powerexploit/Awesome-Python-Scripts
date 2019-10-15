"""
  In this script we're going to create a simple excel file with 3(Three) columns
  Name | Age | Gender
"""



# xlwt module helps make a new excel file 
import xlwt

# create a dictionary with information
DATA_ = {
	'Person1' : {
		'Name' : 'Bill Gates',
		'Age' : 63,
		'Gender' : 'Male'
	},
	'Person2' : {
		'Name' : 'Sheryl Sandberg',
		'Age' : 50,
		'Gender' : 'Female'
	},
	'Person3' : {
		'Name' : 'Tim Cook',
		'Age' : 58,
		'Gender' : 'Male'
	},
}

# first create a new workbook
workbook = xlwt.Workbook()

# add a new sheet to the workbook
sheet = workbook.add_sheet('Sheet1')

# create columns 
sheet.write(0,0,'Name')
sheet.write(0,1,'Age')
sheet.write(0,2,'Gender')


# we will keep counter running until we loop through all the persons inside DATA_
counter = 1

# now lets get the details from the DATA_ dict and insert them into our excel sheet
for k, v in DATA_.items():
	sheet.write(counter, 0, v['Name'])
	sheet.write(counter, 1, v['Age'])
	sheet.write(counter, 2, v['Gender'])
	
	# now increment the counter each time
	# this will make sure that information are added on new line for each person
	counter += 1

# time to save the workbook
workbook.save('details.xls')
