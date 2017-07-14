import datetime
import pandas as pd


class Chat:
    def __init__(self, path):
        with open(path) as f:
            # Strips 'n' and only returns non empty lines
            self.__content = [x.strip() for x in f.readlines()]

        self.__content[0].split(', ')
        self.__msg, self.__ws_notices = [], []
        self.__index = 0

        # Function to append a multiple line chat to single line
        # 7/9/17, 7:37 PM - Shibu Thomas: Total expence at costco after deduction of carrot & cucumber( $11) =$89
        # Brancroft Home Hardware =$31
        # Becomes
        # 7/9/17, 7:37 PM - Shibu Thomas: Total expence at costco after deduction of carrot & cucumber( $11) =$89\nBrancroft Home Hardware =$31
        def append_to_prev_msg():
            # global index, content
            self.__content[self.__index - 1] += '\n' + self.__content[self.__index]
            del self.__content[self.__index]
            self.__index -= 1

        while self.__index < len(self.__content):
            #     print(index, len(content))
            # Some of the elements are just blank lines.
            # Which we remove from our list and append them to the previous element
            # 7/9/17, 6:41 PM - Anish: My expenses:
            #
            # Camp site booking: $535.
            # Additional Parking: $22
            # Fire wood: $7
            # Becomes
            # 7/9/17, 6:41 PM - Anish: My expenses:
            # Camp site booking: $535.
            # Additional Parking: $22
            # Fire wood: $7
            if not self.__content[self.__index]:
                append_to_prev_msg()
            elif self.__content[self.__index][0] == "[":
                print("found msg that is a resend")
            else:
                try:
                    # Parse date and time
                    # 7/9/17, 11:33 AM - Diana Susan: Hi iam here
                    # Split the string and taking the first element in list which will be date
                    # See if we can parse the date.
                    # Value error arrises becuase the message doesn't have date
                    temp = self.__content[self.__index].split(' - ')
                    date = datetime.datetime.strptime(temp[0], "%d/%m/%y, %I:%M %p")

                    # Parse Name
                    # 7/9/17, 11:33 AM - Diana Susan: Hi iam here
                    # Split and take the first element should be name

                    # Check if a its a whatsapp notice
                    # 7/9/17, 12:30 PM - Messages to this group are now secured with end-to-end encryption. Tap for more info.
                    # 7/9/17, 12:30 PM - Jhon added Nikhil
                    # 7/11/17, 3:08 PM - Manju Joseph changed this group's icon
                    temp = temp[1].split(':')
                    if len(temp) is 1:
                        self.__ws_notices.append({'date': date, 'message': temp[0]})
                    else:
                        self.__msg.append({'date': date, 'name': temp[0], 'message': temp[1]})
                        #                 print({'date':date,'name': temp[0],'message':temp[1]})
                except ValueError:
                    print("ValueError", self.__index)
                    append_to_prev_msg()
            self.__index += 1

    def df(self):
        return pd.DataFrame(self.__content), pd.DataFrame(self.__ws_notices)
