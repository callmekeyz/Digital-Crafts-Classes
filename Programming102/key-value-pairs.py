movie = {
    "name":"Star Wars",
    "episode":4,
    "year":"1977",
    "villians":["vader","tarking"],
    "heros":["luke","leia","han"]
}

print(movie)

print(movie["year"])
print(movie["heros"])

bad_guys = movie["villians"]
print(bad_guys)
print(bad_guys[1])
bad_guys.append("jabba")
print(movie)

search = "heros"
print(movie[search])

if "year" in movie:
    print("yes this has a year")