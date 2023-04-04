import math

def magic_square(n):
	magic=[[0 for i in range(n)] for i in range(n)]

	i,j=n//2,n-1
	count=1
	while(count<=n*n):
		
		if i==-1:
			if j==n:#case of i and j both
				i,j=0,n-2
			else:#just i 
				i=n-1
		elif j==n:#just j
			j=0

		if(magic[i][j]!=0):
			i+=1
			j-=2
			continue   #skips the rest of the code to run the above conditions again
		else:
			magic[i][j]=count;
		
		"""updation part of code"""
		i-=1
		j+=1
		count+=1





	print("\n","_"*(6*n-2))
	for i in range(n):
		for j in range(n):
			
			print("|",magic[i][j],"|",end=" ")

		print("\n","_"*(6*n-2))

	print("\nThe sum of any row/column/diagonal is ",n*(n**2+1)//2)


magic_square(3)

