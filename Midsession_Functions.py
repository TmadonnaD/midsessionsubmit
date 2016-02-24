
# ----------------------------------------------------------
# 1.
# Create a function called convert_to_seconds that has
# parameters hours, minutes, and seconds, and returns the
# value in seconds.
# ----------------------------------------------------------

# PSEUDOCODE/notes:

# ~ take input for hours/minutes to convert.
# ~ calculate number of seconds


 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#CODE:

seconds = minutes /60
minutes = hours / 60 
hours  =  minutes * 60

def convert_to_seconds (hours, minutes, seconds):
	return  #seconds

seconds = float(raw_nput("Enter the number of minutes to convert to seconds: "))


input = 0.00
raw_input * 60 # for minutes
raw_input / 60  #for hours


inches = convert_to_second(hours, minutes, seconds)

print(" {} hours = {} seconds.".format(feet,inches))

# ----------------------------------------------------------
# 2.
# Create a function called convert_to_inches that has
# parameters feet and inches, and returns the value
# in inches.
# ----------------------------------------------------------

# PSEUDOCODE/notes:

#  ~define inch, feet
#  ~take input for "number of feet to comvert"
#  ~multiply feet by inch
#  ~print out result, in inches
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CODE:


inch = 12

def convert_to_inches(feet,inch):
	return feet * inch

feet = (input("Enter the number of feet you would like to convert: "))



inches = convert_to_inches(feet,inch)

print(" {} feet = {} inches.".format(feet,inches))

# Notes 
#  I get EOF error msg =( =( =(
