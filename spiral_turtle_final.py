'''
	1  2  3  4
	5  6  7  8 
	9 10 11 12
   13 14 15 16

   go spirally starting from 1 end at 10

   this time we will animate it using turlte module

'''
import turtle, random

turtle.bgcolor("black") # dafault color is white
seurat=turtle.Turtle()

width,height=5,7
dot_distance = 25

seurat.penup()
color_list=["white","violet","indigo","blue","green","yellow","orange","red","grey","brown","pink"]

seurat.setpos(-250,250) # DEFAULT POSTION IS AT CENTRE but we need it at topmost left 


def spiral( m, n):
	k,l=0,0
	# k --> index of startng row       m --> index of ending row
	# l --> index of startng column    n --> index of ending column
	seurat.color("white")

	flag = 0
	while(k < m and l < n):
		if flag==1:
			seurat.rt(90)
		
		seurat.color(random.choice(color_list))
		for i in range(l, n): 
			
			seurat.dot() # first prints dot then pens up automatically and then moves as per instructions given
			seurat.fd(dot_distance)
		k+=1 # incrementing the row 
		flag = 1

		seurat.rt(90)

		seurat.color(random.choice(color_list))
		for i in range(k , m): 			  
			seurat.dot()
			seurat.fd(dot_distance)
		n-=1 # decrementing the column
		
		seurat.rt(90)

		if k<m:
			seurat.color(random.choice(color_list))			
			for i in range(n-1, l-1, -1): 
				seurat.dot()
				seurat.fd(dot_distance)
			m-=1
		
		seurat.rt(90)

		if l<n:
			seurat.color(random.choice(color_list))			
			for i in range(m-1, k-1,-1):
				seurat.dot()
				seurat.fd(dot_distance)
			l+=1


spiral(10,10)
turtle.done()