# Project #1: Letter Counter
def letter_counter(txt = "", dict = {}):
  for char in txt:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  # print(dict)
  return dict

text = input()
dic = {}
print(letter_counter(text, dic))

# Project #2: Spelling Backwards
def spell(txt):
  if txt == "":  
    return txt
  else:
    # print(txt[len(txt) - 1])
    return spell(txt[0: len(txt) - 1])

txt = input()
print(spell(txt))

# Project #3: Alien Game
class Enemy:
	name = ""
	lives = 0
	def __init__(self, name, lives):
		self.name = name
		self.lives = lives

	def hit(self):
		self.lives -= 1
		if self.lives <= 0:
			print(self.name + ' killed')
		else:
			print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
	def __init__(self):
		super().__init__('Monster', 3)
  
	def hit(self):
		super().hit()

class Alien(Enemy):
	def __init__(self):
		super().__init__('Alien', 5)
  
	def hit(self):
		super().hit()


m = Monster()
a = Alien()

while True:
	x = input()
	if x == 'exit':
		break
	elif x == 'laser':
		a.hit()
	elif x == 'gun':
		m.hit()

# Project #4: Registration Problem
def registration():
  try:
    name = input()
    count = 0
    for letter in name:
      count += 1
      
    if count > 3:
      print("Account Created")
    else:
      raise Exception
  except:
    print("Invalid Name")

registration()

# Project #5: Title Encoder

def title_encoder():
  file = open("/usercode/files/books.txt", "r")
  for x in file:
    title = x.split()
    for a in title:
      print(a[0], end = "")
  file.close()

print(title_encoder())

