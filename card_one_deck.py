# create cards
from random import shuffle
from functools import reduce
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
import numpy as np

cards = [list(range(1,14)) for _ in range(4)] + [[0,0]] # the four jokers
cards = reduce(lambda x,y: x+y, cards, [])				  # merge into one list
print(cards)

def pick_cards(cards, size):
	shuffle(cards)
	return cards[:size]

def count_bomb(cards):
	d = {}
	for i in cards:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	count = 0
	for key in d:
		if d[key] >= 4:
			count += 1

	if 0 in d and d[0] == 2:
		count += 1

	return count

def plot_normal(mu=0, variance=1):
	mu = 0
	variance = 1
	sigma = math.sqrt(variance)
	x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
	plt.plot(x,mlab.normpdf(x, mu, sigma))


result1 = [0 for i in range(6)]      # landlord 
result2 = [0 for i in range(6)]		 # farmer
for i in range(10**6):
	t1 = pick_cards(cards, 17)
	t2 = pick_cards(cards, 20)
	b1 = count_bomb(t1)
	b2 = count_bomb(t2)
	result1[b1] += 1
	result2[b2] += 1

print("landlord, " , result1)
print("farmer, " , result2)
# above_3 = 0
# for i in range(3,9):
	# above_3 += result[i]

# print(above_3 / sum(result))

plt.plot(list(range(0,6)), list(map(lambda x: x/sum(result1), result1)), label="Landlord", color='red')
plt.plot(list(range(0,6)), list(map(lambda x: x/sum(result2), result2)), label="Farmer", color='blue')
mu = 3
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma), label="normal", color='green')
plt.ylabel('Percentage')
plt.xlabel('Bomb count')
plt.title("Distribution of bombs for landloard and regular player, and distribution of normal")
plt.axis([0, 6, 0, 1])
plt.show()