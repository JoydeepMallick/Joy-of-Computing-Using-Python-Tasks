'''
	1  2  3  4
	5  6  7  8 
	9 10 11 12
   13 14 15 16

   go spirally starting from 1 end at 10

'''

def spiral( m, n, a):
	k,l=0,0
	# k --> index of staritng row
	# l --> indix of stritng column

	while(k < m and l < n):
		# printing the first row form the remaining rows
		for i in range(l, n): #n denotes max column in each row
			print(a[k][i], end=" ")#--> * * * * * * *

		k+=1 # incrementing the row 

		for i in range(k , m): # max no of rows				  
			print(a[i][n-1], end=' ') # n-1 since indexing starts from 0  * * * * *
			
		n-=1 # decrementing the column
		
		if k<m:
			# printing lst row from remaingin rows
			for i in range(n-1, l-1, -1): # 2nd last column to 2nd column
				print(a[m-1][i], end=' ')
			m-=1
		if l<n:
			#printing the first column from remaing columns
			for i in range(m-1, k-1,-1):
				print(a[i][l],end=' ')
			l+=1


a=[]
count=1
for i in range(4):
	l=[]
	for i in range(4):
		l.append(count)
		count+=1
	a.append(l)

spiral(4,4,a)