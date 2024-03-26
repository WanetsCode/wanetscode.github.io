#############################################
#███████████████████████████████████████████████#
#█─▄▄▄▄█▄─▄▄─█▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀█▄─▀█▀─▄██─▄▄─█#
#█▄▄▄▄─██─▄▄▄██─▄█▀██─█▄▀─███─██─██─█▄█─███─▄█▀█#
#█▄▄▄▄▄█▄▄▄███▄▄▄▄▄█▄▄███▄██▄▄▄▄██▄▄▄█▄▄▄██▄▄▄▄█#
#███████████████████████████████████████████████#
#         Made By Wanets. Published         #
#            with ❤️ on GitHub              #
#############################################

# So, we're starting with the description:
# open the README file to read about this code
import datetime
# Making database is easy...on SQL, but this is a python code so...
import os
amount = int(input("Type the amount money spend: (Example: 30)"))
amountCur = input("Type the currency mark (Example: $) The mark will become $ if skipped. Please use the same marks for same uses.")
# Now we have to make "The mark will become $ if skipped.":
if amountCur == "":
    amountCur = "$"
#DONE!
# And lastly...THE SAVING PART!!!
use = str(input("Type the use of the money (Example: GitHub_Premium_Subscribtion)"))
# Now we have to deal with saving the data:
with open(f"{use}.txt", "a") as f:
    # Get the current date and time
    now = datetime.datetime.now()
    now = now.strftime("%y.%m.%d %H:%M")
    f.write(f"{now} - {amount}{amountCur} _____________________________________________________")
    print(f"You have registered {amount}{amountCur} for {use}")
