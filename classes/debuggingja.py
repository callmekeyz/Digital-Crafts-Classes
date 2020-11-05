def pushZerosToEnd(arr, n): 
	count = 0
	

	for i in range(n): 
		if arr[i] != 0:
			arr[count] = arr[i] 
			count+=1
	
	
	while count < n: 
		arr[count] = 0
		count += 1
		
# Driver code 
arr = [2, 19, 3, 4, 0, 0, 9, 10, 0, 5, 0, 6] 
n = len(arr) 
pushZerosToEnd(arr, n) 
print("Array after pushing all zeros to end of array:") 
print(arr) 





def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 7:
      count = count + 1

  return count

print(list_count_4([7, 3, 10, 7, 4,15,3,7,7]))

