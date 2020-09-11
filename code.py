def oddoreven(numbers):
	if len(numbers)>0:
		result =[]
		for i in numbers:
			if i%2 ==0:
				result.append(0)
			else:
				result.append(1)
		print(result)		
	else:
		print("Input error")				


numbers = [1,2,3,4,4,4,4]	
oddoreven(numbers)	
