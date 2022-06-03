file_read = open("README.txt")
file_write = open("副本", "w")
while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)
file_read.close()
file_write.close()
