import commons

report_list = []

def part1():
	with commons.get_file("03") as file:
		createList(file)
		gamma = getGammaRate(report_list)
		epsilon = getEpsilonRate(gamma)
		print(int(gamma, 2) * int(epsilon, 2))

def createList(file):
	for row in file:
		report_list.append(row.replace('\n', ''))

def getGammaRate(remain_list, equal = '0'):
	count0 = 0
	count1 = 0
	byte = ''
	for i in range(len(remain_list[0])):
		for j in range(len(remain_list)):
			if remain_list[j][i] == '0':
				count0 +=1
			elif remain_list[j][i] == '1':
				count1 +=1
		if count0 > count1:
			byte += '0'
		elif count0 < count1:
			byte += '1'
		else:
			byte += equal
		count0 = 0
		count1 = 0
	return byte

def getEpsilonRate(gamma:str):
	epsilon = gamma.replace('0','A').replace('1','0').replace('A', '1')
	return epsilon

def part2():
	oxygen = getOxigenRate()
	CO2 = getCO2Rate()
	print(int(oxygen, 2)*int(CO2, 2))

def getOxigenRate():
	oxigenList = report_list
	for i in range(len(oxigenList[0])):
		bitCriteria = getGammaRate(oxigenList, equal='1')
		if len(oxigenList) != 1:
			oxigenList = list(filter(lambda byteItem: byteItem[i] == bitCriteria[i], oxigenList))

	return oxigenList[0]

def getCO2Rate():
	CO2List = report_list
	for i in range(len(CO2List[0])):
		bitCriteria = getEpsilonRate(getGammaRate(CO2List, equal = '1'))
		if len(CO2List) != 1:
			CO2List = list(filter(lambda byteItem: byteItem[i] == bitCriteria[i], CO2List))
	return CO2List[0]

def main():
	print("PART 1 -------")
	part1()
	print("PART 2 -------")
	part2()
	






if __name__ == "__main__":
	main()


