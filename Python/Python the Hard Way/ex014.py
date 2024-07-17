from sys import argv

script, user_name = argv

prompt = '>'

print "Hi %s, I'm the %s script" % (user_name, script)
print "I'd like to ask you a questions"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s ?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me
You live in %r. I don't know where that is
And you have %r computer
""" % (likes, lives, computer)

#the difference between raw_input() and input(prompt) is that first treats it as a string and the second an expression.