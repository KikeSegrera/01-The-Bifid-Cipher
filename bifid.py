#The Bifid Cipher
import fileinput

def bifid(option,tableau,text):
	rows, cols, coord = [], [], []
	result = ''

	if option == "ENCRYPT":
		text = text.replace(' ','')
		for t in text:
			for i in range(0,len(tableau)):
				for j in range(0,len(tableau[0])):
					if tableau[i][j] == t:
						rows.append(i)
						cols.append(j)
		coord = rows + cols
		for r in range(0,len(coord),2):
			result = result + tableau[coord[r]][coord[r+1]]
		return result

	elif option == "DECRYPT":
		for t in text:
			for i in range(0,len(tableau)):
				for j in range(0,len(tableau[0])):
					if tableau[i][j] == t:
						coord.append(i)
						coord.append(j)
		length = int(len(coord)/2)
		rows = coord[0:length]
		cols = coord[length:len(coord)]
		for r in range(0,len(rows)):
			result = result + tableau[rows[r]][cols[r]]
		return result

lines = []
tableau = [['E','N','C','R','Y'], ['P','T','A','B','D'], ['F','G','H','I','K'], ['L','M','O','Q','S'], ['U','V','W','X','Z']]

for line in fileinput.input():
	line = line.replace('\n','')
	lines.append(line)

print(bifid(lines[0],tableau,lines[1]))
