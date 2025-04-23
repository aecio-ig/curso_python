import secrets


random = secrets.SystemRandom

random.seed(5)

r_randou = random.randrange(10,20)
print(r_randou)

r_randou = random.randint(10,20)
print(r_randou)

nomes = ['aecio', 'tiana', 'greg', 'minhoco']

print(random.shuffle(nomes))

print(nomes)

print(random.choices(nomes))



