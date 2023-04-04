

def player(p):
    p = p.lower()
    p = p.replace(" ","") # trimming unwanted spaces
    return(list(p))

def remove_matching_letter(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                c = l1[i]
                l1.remove(c)
                l2.remove(c)
                lst = l1+["*"]+l2
                return [lst, True]
    lst = l1 + ["*"]+l2 # asterisk seerve as a breakpoint in concatenation
    return [lst, False]

print("\nThe FLAMES game !!!\n")

p1 = input("Enter first player's name : ")
p2 = input("Enter second player's name : ")

l1, l2 = player(p1), player(p2)
proceed = True
while proceed:
    ret_list = remove_matching_letter(l1, l2)
    con_list = ret_list[0]
    proceed = ret_list[1] # true or false
    star_index = con_list.index("*") # helps in breaking he concatenated list again
    l1 = con_list[:star_index]
    l2 = con_list[star_index+1:]
    
count = len(l1) + len(l2)
result = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']

while(len(result) > 1): 
    split_index = (count % len(result)) - 1 # index = positon -1
    if split_index >= 0:
        result = result[split_index + 1 : ] + result[ : split_index]
    else:
        result = result[:split_index] # last element deleted from result

print("\n",p1,"and",p2,"are",result[0])
