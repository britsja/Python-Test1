f = open('newfile.txt', 'a')
lines = ['Hello', 'World','welcome', 'to', 'File IO' ]
text = ' '.join(lines)
f.writelines(text)
f.close