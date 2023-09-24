import sys 

n,m = map(int, sys.stdin.readline().rstrip().split())
pokemons1 = {}
pokemons2 = {}

for i in range(n):
  pokemon = sys.stdin.readline().rstrip()
  pokemons1[pokemon] = i+1
  pokemons2[str(i+1)] = pokemon

for _ in range(m):
  key = sys.stdin.readline().rstrip()
  if key.isalpha():
    print(pokemons1[key])
  else:
    print(pokemons2[key])