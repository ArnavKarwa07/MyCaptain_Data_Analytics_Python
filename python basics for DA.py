#create lists
a = list(range(4,9))
print(a)
b = list(range(4,9,2)) #3rd number is stepsize(number to be skipped)
print(b)

print(a[1::2])#3rd number is stepsize(number to be skipped)
c = a + b
print(c)
print("SrNo \t","Number" )
i=1
for j in a:
    print(i,"\t\t",j)
    i+=1
#pop is removing by position(default is last element)
#remove is removing by value
#append is add element in the end
#insery is add element at specific location .insert(element,position)
#sort is sort in ascending

#dictionary has no positional argument
dict1 = {"name": "Arnav", "value":"7 crore"}
        #key      #value
print(dict1)
print(dict1["name"])
dict1["age"] = 18 #add element as it is
print(dict1)
dict1["value"] = "8 crore" #update value
print(dict1)
dict1.pop("age") #remove
print(dict1)
for key in dict1:
    print(key,":", dict1[key])