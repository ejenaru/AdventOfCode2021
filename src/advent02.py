import commons

class Submarine:
	x= 0
	y = 0
	aim = 0
	
	def forward(self, dist):
		self.x +=dist
	def up(self, dist):
		self.y -=dist	
	def down(self, dist):
		self.y +=dist
	
	def forward2(self, dist):
		self.x +=dist
		self.y += self.aim*dist
	def up2(self, dist):
		self.aim -=dist
	def down2(self, dist):
		self.aim +=dist

	def getResult(self):
		return self.x*self.y


commands = {
	"forward": 0,
	"up": 0,
	"down" : 0
}

def part11():
	sub = Submarine()
	with commons.get_file() as file:
		for line in file:
			command = line.split()[0]
			data = int(line.split()[1])
			sub.__getattribute__(command)(data)

	print("Parte 1 => " + str(sub.getResult()))


def part1():
	sub = Submarine()
	with commons.get_file() as file:
		for line in file:
			command = line.split()
			commands[command[0]] += int(command[1])
	print(commands)
	sub.forward(commands["forward"])
	sub.up(commands["up"])
	sub.down(commands["down"])
	print("Parte 1 => " + str(sub.getResult()))

def part2():
	sub = Submarine()
	with commons.get_file() as file:
		for line in file:
			command = line.split()[0]
			data = int(line.split()[1])
			sub.__getattribute__(command + "2")(data)

	print("Parte 2 => " + str(sub.getResult()))


def main():
	part11()
	part2()
	






if __name__ == "__main__":
	main()


