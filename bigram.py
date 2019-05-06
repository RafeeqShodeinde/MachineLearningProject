
######## BIGRAM IMPLEMENTATION###########
import re
import csv


num = 1
row = ["Id","Expected"]
with open('bigram.csv', 'w', newline='') as csvfile:
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


	tempLib = {}
	beforeLib = {}
	afterLib = {}
	for i in target:
		tempLib = {i:{}}
		beforeLib.update(tempLib)
		afterLib.update(tempLib)	
	tempLib.clear()
	
	##################### BIGRAM IMPLEMENTATION #####################

	############# TRAINING DATA PROCESSING ############
	for t in target:		
		for i in range(len(words)):	
			
			if (t == words[i]) and (words[i-1] not in beforeLib[t]):		
				beforeLib[t][words[i-1]] = 1
			
			elif (t == words[i]) and (words[i-1] in beforeLib):
				beforeLib[t][words[i-1]] += 1
			
			elif (t == words[i]) and (words[i+1] not in afterLib[t]):
				afterLib[t][words[i+1]] = 1
			
			elif (t == words[i]) and (words[i+1] in afterLib):
				afterLib[t][words[i+1]] += 1
				
			

	fileReader.close()
	
	######### TEST DATA PROCESSING ############# 
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
				
				###Computation###
				for j in beforeLib[study1]:
					if (j == checkWord):
						numValueBefore = beforeLib[study1][j]
					else:
						numValueBefore = 1
						
				for k in afterLib[study1]:
					if (k == checkWord2):
						numValueAfter = afterLib[study1][k]
					else:
						numValueAfter = 1 
					
				for l in beforeLib[study2]:
					if (l == checkWord):
						numValue2Before = beforeLib[study2][l]
					else:
						numValue2Before = 1
								
				for m in afterLib[study2]:
					if (m == checkWord2):
						numValue2After = afterLib[study2][m]
						print(numValue2After)
					else:
						numValue2After = 1
					
				probBefore = (numValueBefore)/(numValueBefore + numValue2Before + 1)
				probAfter = (numValueAfter)/(numValueAfter + numValue2After + 1)
					
				probBeforeOther = (numValue2Before)/(numValue2Before + numValueBefore + 1)
				probAfterOther = (numValue2After)/(numValue2After + numValueAfter + 1)
					
				alpha = probAfter * probBefore
				beta = probBeforeOther * probAfterOther  
				totalProb = alpha/(alpha + beta)
				
				newRows = [num,totalProb]
				writer.writerow(newRows)
				num += 1
	fileReader.close()
csvfile.close()

	
	

	
	

	
	








