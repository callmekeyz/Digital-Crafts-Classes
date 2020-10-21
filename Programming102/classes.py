class person:
    def __init__(self,name,age,height="normal"):
        print(self)
        print("you created a new instance of a person.")
        self.name = name
        self.age = age
        self.height = height

keyz = person("keyz",32,"short")
lyric = person("lyric",6)

print(f"wow {keyz.name} you are {keyz.age} years old")
print(keyz.height)