# Define a function that returns formatted minutes and seconds

###################################################
# Time formatting function
# Student should enter function on the next lines.
def   format_time(sec):
      min=sec//60
      sec=sec%60
      hours=min//60
      min=min%60
      print("hours: "+str(hours))
      print("minutes: "+str(min))
      print("seconds: "+str(sec))
        


###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds
