import sys
def receiveDiffInputs(name, *touples, **dicts):
	print 'My Hello World Program is: '+ name;
	for t in touples:
		print t
		print 'done'

 	for d in dicts:
 		print (d, dicts[d])
 		print (d)
 		print (dicts[d])
 		
 def receiveDiffInputs1(name, **dicts):
	print 'My Hello World Program is: '+ name;
 	for d in dicts:
 		print (d, dicts[d])
 		print (d)
 		print (dicts[d])		

receiveDiffInputs('Test', 1,2,3,"r", java=1,python=0)	
receiveDiffInputs1('Test', java=1,python=0)	