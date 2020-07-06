
def __drawHorizontalLine():
	s = "---"
	for i in range(9):
		s = s + "---"
	s = s + "-"
	print(s)


def displayGrid(_data):
	__drawHorizontalLine()
	for r in range(9):
		s = "|"
		for c in range(9):
			if _data[r][c] == 0:
				s = s + " " + " " + " "
			else:
				s = s + " " + str(_data[r][c]) + " "
			if( (c + 1)%3 == 0 ):
				s = s + "|"
		print(s)
		if((r+1)%3 == 0):
			__drawHorizontalLine()

def displayGridLineByLine(_data):
	__drawHorizontalLine()
	for r in range(9):
		s = "R" + str(r) + " : "
		for c in range(9):
			# s += "    C" + str(c)
			s += str(_data[r][c]) + "."
		print(s)

def displayLineByLine(_data):
	__drawHorizontalLine()
	for i in range(len(_data)):
		s = str(i + 1) + " -> "
		s += "\t" + str(_data[i])
		print(s)