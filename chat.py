with open('./_chat.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
c, r = 0, 0
increment = ""
for x in content:
    if (x.find('Chinku') != -1):
        c += 1
        increment = "c"
    elif (x.find('Roney') != -1):
        r += 1
        increment = "r"
    elif (x.find('‎Messages you send to this chat and calls are now secured with end-to-end encryption.') == -1) & len(
            x) > 0:
        if (increment == 'r'):
            r += 1
        else:
            c += 1
print("Chinku ", c)
print("Roney ", r)
