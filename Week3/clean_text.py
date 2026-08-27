sn=" I  Love   python   tooooo      much"
raw_data=sn.split(" ")

word=[]
for text in raw_data:
	if text:
		word.append(text)

clean_data=" ".join(word)
print("Clean Data: ", clean_data)
