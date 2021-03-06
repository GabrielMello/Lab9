############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
print "What is your temperature?"
humanTemperature = raw_input()
if humanTemperature > 105:
    print "Have you been sick in the past 24 hours?"
else:
    print "You do not need to be admitted to the hospital."
userSicktime = raw_input()
if userSicktime == "yes" :
    print "Have you recently traveled to West Africa?"
else:
    print "You only have a fever"
userAfrica = raw_input()
if userAfrica == "yes":
    print "You must immediately go to the hospital"
else:
    print "You are fine"
    