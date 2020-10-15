first ='look a string'
second = "a string with double quotes"
third = '''
I want to cross spaces
now I am down here
'''

fourth = "'" this is going to
be 
spaced down "'"

print("hello" + " " +"world")

message = "Hello World!"
#very bad not working
# bob = "YES!"
# bob = 42 + bob
print (message)

name = "Mikeya"
#f string
combined = f "I want to say {message} to {name}."
print(f"I want to say {message" to {name}.)

#
adj = "Awesome"
# new_string = "Hey this is %s, and I like it" thing
print("Hey this is %s, amd I like it" % adj)

print ("I want to tell %s %s and Hey this is %s"% (name,message,adj))

haiku = "Haikus are easy.\nBut sometimes they dnot make sense.\n\Refridgerator."
print(haiku)
