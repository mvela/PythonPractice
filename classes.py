#basic class

class animal:
	def __init__(self, anim, gen, weig):
		self.animal = anim
		self.gender = gen
		self.weight = weig

animal1 = animal("dog", "male", 56)

print(animal1.animal, animal1.gender, animal1.weight)

animal1.animal = "cat"
print(animal1.animal, animal1.gender, animal1.weight)
