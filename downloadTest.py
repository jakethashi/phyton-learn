file = open("test.txt", "r")
content = file.read()

content = content.replace("some", "jak se vede")
print(content);