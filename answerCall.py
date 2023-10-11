# answerCall.py
# by Jeshua G.V

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)



# Write function defintion: answerCall()
def answerCall (caller_code, sameAreaCode, cur_time):
    response = True
    hour, minute = cur_time.split(":")
    if hour >= "21":
        response = False
    elif caller_code == "R" or caller_code == "F":
        response = True
    else:
        response = False

        if caller_code == "U" and sameAreaCode:
            response = True
        else:
            response = False
    return response

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    answerCall("U", False, "09:00")
