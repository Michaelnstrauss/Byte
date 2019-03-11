

users = [
    {'username': 'samuel', 'tweets': ['I love cake', 'I love pie']},
    {'username': 'katie', 'tweets': ['I love my cat']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo_luvr', 'tweets': ['dogs are the best']},
    {'username': 'guitar_gal', 'tweets': []}
]


inactive_users = list(filter(lambda user: not user['tweets'], users))
inactive_users2 = [user['username'].upper() for user in users if not user['tweets']]
print(inactive_users2)
#print(inactive_users)

bartldoo = list(map(lambda user: user['username'].upper(), 
    filter(lambda u: not u['tweets'], users)))

#print(bartldoo)

