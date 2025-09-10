#♦️Number Generation
import random
#1. random.random() = returns a random float from 0.0 to 1.0 (excludes 1.0)
print(f'random.random = {random.random()}')
print(f'random.random * 5 = {random.random() * 5}') #inc range to 5
print(f'random.random * 100 = {random.random() * 100}') #inc range to 100

#2. random.uniform(a, b) = returns a random float between a to b
print(f'random.uniform(1, 10) = {random.uniform(1,10)}')

#3. random.randint(a, b) = returns a random integer between a to b (both inclusive)
print(f'random.randint(1,10) = {random.randint(1,10)}')

#4. random.randrange(start, stop, step) = returns a random integer from the range(start, stop, step)
print(f'random.randrange(1, 10, 2) = {random.randrange(1, 10, 2)}')

#♦️Choice and sampling
#1. random.choice(sequence) = returns a random element from the non-empty sequence
colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'orange']
print(f'random.choice(colors) = {random.choice(colors)}')

#2. random.choices(sequence, weights=None, k=1) = Returns a random sample from a sequence of length k with replacement(same sample can be rechoosen)
print(f'random.choices(colors, k=3) = {random.choices(colors, k=3)}')

#3. random.sample(sequence, k) = Returns a random sample from a sequence of length k without replacement(same sample cannot be rechoosen)
print(f'random.sample(colors, k=3) = {random.sample(colors, k=3)}')

#4. random.shuffle(sequence) = Shuffles the sequence in place
print(f'Before shuffle: {colors}')
random.shuffle(colors)
print(f'After shuffle: {colors}')

#♦️ State control
#1. random.seed() = same results every time the code is run
random.seed(10)
print(f'random.random with seed 10 = {random.randint(1, 10)}')

# There are 20 participants (named "P1" to "P20").
# Each participant’s name is placed in the lottery box.
# Step 1: Use random.choices() to pick 5 names with replacement (these are raffle tickets, so the same participant can appear more than once).
# Step 2: From those 5 names, use random.sample() to select 2 unique winners.
# Step 0: Create participants list
participants = [f"P{i}" for i in range(1, 21)]

# Step 1: Pick 5 names with replacement
raffle_draw = random.choices(participants, k=5)
print("Raffle tickets:", raffle_draw)

# Step 2: Pick 2 winners (unique) from those 5
winners = random.sample(raffle_draw, k=2)
print("Final winners:", winners)

