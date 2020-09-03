# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

#open the text in the file
#ignore the bad characters
f = open("ciphertext.txt", "r")
ignore = ["1", ":", ";", ",", ".", "\n", "—", "?", "!", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\"", " ", "'"]

#create a cache
#read the text and
#if x is in ignore then move on
#if x is in the cache then keep going
#otherwise add x to the cache
cache = {}
for x in f.read():
	if x in ignore:
		continue
	if x in cache:
		cache[x] += 1
	else:
		cache[x] = 1

#intialize the count to 0
#count the values
count = 0
for k in cache.values():
	count += k

#sort the items in the cache
a = sorted(cache.items(), key=lambda kv: (kv[1], kv[0]))
code = ["Z", "X", "J", "Q", "V", "K", "P", "C", "Y", "M", "B", "F", "G", "U", 'W', "L", "D", "S", "I", "R", "N", "H", "O", "A", "T", "E"]

#intialize a table
decode_table = {}
#reset count to 0
counter = 0

#for each item in the sorted cache
#and for each x in the item
#count x
for item in a:
	for x in item[-2]:
		decode_table[x] = code[counter]
		counter += 1

# decode 
# return result
def decode(s):
	r = ""
	for c in s:
		if c in decode_table:
			r += decode_table[c]
		else:
			r += c
	return r

f.close()

fx = open("ciphertext.txt", "r")
print(decode(fx.read()))
fx.close()

