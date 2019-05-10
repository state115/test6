from sys import argv
import os

myfile = os.path.basename(os.path.realpath(__file__))

print(os.path.realpath(__file__))



user_name = 'yin'

prompt = '> '  # 将用户提示符设置为变量 prompt，
print("Hi %s, I'm the %s script." % (user_name, myfile))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt) # 将用户输入时的提示符设置为变量 prompt，

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = raw_input(prompt)

print(""" 
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer. Nice. 
""" % (likes, lives, computer))

# 当你运行这个脚本时，记住你需要把你的名字赋给这个脚本，让 argv 参数接收到你的名称。