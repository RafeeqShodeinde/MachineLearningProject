import re
import csv


num = 1
row = ["Id","Expected"]
with open('unigram.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(row)
	
	##############READS TRAIN DATA##########
	fileReader = open('train.txt','r')
	lines = fileReader.read()
	target = ['a','á','ais','áis','aisti','aistí','ait','áit','ar','ár','arsa','ársa',
			'ban','bán','cead','céad','chas','chás','chuig','chúig','dar','dár','do',
			'dó','gaire','gáire','i','í','inar','inár','leacht','léacht','leas','léas',
			'mo','mó','na','ná','os','ós','re','ré','scor','scór','te','té','teann',
			'téann','thoir','thóir']
                
	words = re.split("[, \@\"\'\-!?:.+/\[\])(><\n_]+", lines)
	words = [w.strip() for w in words]
	
	unigramLib = {}

	##################### UNIGRAM IMPLEMENTATION ##############
	for t in target:
		count = 0
		for word in words:
			if (t == word):
				count += 1
		unigramLib[t] = count
	
	fileReader.close()

	count1 = 0
	count2 = 0
	total = 0
	prob = 0
	
	testFileReader = open('test.txt','r')
	testLines = testFileReader.read()
	testWords = re.split("[, \@\"\'\-!?:.+/\[\])_(><\n]+", testLines)
	testWords = [w.strip() for w in testWords]
	testWords.remove("")
	
	
	for i in range(len(testWords)):
		if ((len(testWords[i]) >= 1) and testWords[i] != "\n"):
			if (testWords[i][0] == '{'):
				checkWord = testWords[i-1]
				checkWord2 = testWords[i+1]
				splitBrace = testWords[i].strip('{}')
				splitBrace = re.split("\|",splitBrace)
				study1 = splitBrace[0]
				study2 = splitBrace[1]
	
	
				for key, value in unigramLib.items():
					if key == study1:
						count1 = value
					if key == study2:
						count2 = value
				if count1 is not 0 and count2 is not 0:
					total = count1 + count2
					probstudy1 = count1/total
					newRows = [num,probstudy1]
					writer.writerow(newRows)
					num += 1
		
	testFileReader.close()
csvfile.close()
