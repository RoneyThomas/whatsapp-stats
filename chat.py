import csv
import re

with open('./_chat.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
# Remove empty strings
content = list(filter(None, content))
# find messages without date and merge with prev messages

index = 0
while index < len(content):
    # If the len < 10 then there is no date. It can be resend message or continuation of prev mssg.
    print(index)
    print("len val:", len(content))
    if len(content[index]) < 10:
        print("Message is less than 10 chars", content[index])
    # Checking if the msg isn't previously send
    elif content[index][0] == "[":
        print("found msg that is a resend")
        del (content[index])
        index -= 1
    # Whatsapp msg when encryption changes
    # Encrypted msg is delete. To be stored later
    elif content[index].find(
            '‎Messages you send to this chat and calls are now secured with end-to-end encryption.') != -1:
        print("Encryption notice")
        del (content[index])
        index -= 1
    # Check if any msgs start with date
    else:
        date = re.fullmatch(r'\d{4}-\d{2}-\d{2}', content[index][0:10])
        # Checking messages without date. If found merge with prev mssg
        if date is None:
            print("Found prev message ", content[index])
            content[index - 1] += " " + content[index]
            print("new string", content[index - 1])
            del (content[index])
            index -= 1
        else:
            print("Date is not none")
    index += 1

date, time, name, message = [], [], [], []
for index, x in enumerate(content):
    # Create list of dates
    date.append(x[0:10])
    # Create list of times
    colon = [y for y, z in enumerate(x) if z == ':']
    time.append(x[12:colon[2]])
    # Create list of names
    print("index ", index)
    if (len(colon) >= 4):
        name.append(x[colon[2] + 2:colon[3]])
        # Create list of messages
        message.append(x[colon[2] + 2:])
    else:
        # If colon is less than 4
        print(len(colon), x)
print(len(date), len(time), len(name), len(message))

# Outputs to CSV file
with open('output.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    for index, _ in enumerate(content):
        data = (date[index], time[index], name[index], message[index])
        a.writerows([data])
