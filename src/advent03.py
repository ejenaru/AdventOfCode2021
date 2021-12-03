import commons

report_list = []



def part1():
	with commons.get_file("03") as file:
		createList(file)
		gamma = getGammaRate()
		
		epsilon = getEpsilonRate(gamma)
		print(int(gamma, 2) * int(epsilon, 2))

	return
def createList(file):
	for fila in file:
		report_list.append(fila.replace('\n', ''))

def getEpsilonRate(gamma:str):
	epsilon = gamma.replace('0','A').replace('1','0').replace('A', '1')
	return epsilon

def getGammaRate():
	count0 = 0
	count1 = 0
	byte = ''
	for i in range(len(report_list[0])):
		for j in range(len(report_list)):
			if report_list[j][i] == '0':
				count0 +=1
			elif report_list[j][i] == '1':
				count1 +=1
		byte +=  '0' if count0 > count1 else '1'
		count0 = 0
		count1 = 0
	return byte




def part2():
	return



def main():
	part1()
	part2()
	






if __name__ == "__main__":
	main()


