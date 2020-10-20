names = ["Mikeya", "Keyz", "Kiki"]
names.append("keya")
print(names)
names.append("key")
print(names)

names = ["Mikeya","keyz","kiki","keya","key"]

names[2] = ["foo"]
names[4] = ["bar"]
print(names)



while len(names):
    print(names[0])
    del names[0]
