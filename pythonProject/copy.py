file_read = open("README.txt")
file_write = open("README副本", "w")
text = file_read.read()
file_write.write(text)
file_read.close()
file_write.close()
