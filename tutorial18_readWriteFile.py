# create a file
# w: open a file and write it
fw = open('sample.txt', 'w')
fw.write('writing some stuff in my test file\n')
fw.write('I like tuna\n')
fw.close()

# read a file
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
# remember to close
fr.close()