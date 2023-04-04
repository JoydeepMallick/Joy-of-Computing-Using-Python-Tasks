import string
dict={}
letters=string.ascii_letters
for i in range(len(letters)):## cipher by substitution with a before element
    dict[letters[i]]=letters[i-1] # for 1st element index -1 means last element
print(dict)
data=""
with open("sample_edit.txt","r") as f:
    ele=f.read(1)
    while(ele):
        if ele in dict:
            ele=dict[ele]
        ##else same thing
        data+=ele
        ele=f.read(1)
with open("sample_edit.txt","w") as f:
    f.write(data)
#f.close() not needed since with open automatically closes file when it ends



'''below code can replace words in place, not required here'''
# f=open("sample_edit.txt","r+")
# import fileinput
# for line in fileinput.input("sample_edit.txt"):
#     print(line,"\n")
#     #f.write(line.replace(line,dict[line]))
# f.close()