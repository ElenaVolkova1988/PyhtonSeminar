from random import randint as RI

# my_list= []

# for i in range(10):
#     my_list.append(i)
  
# my_list = [ RI(0,10) for i in range(10)]    
# print(my_list)    
  
# получить числа, которые встречаются один раз
data =[1,2,3,5,1,5,3,10]  
my_dict=dict()  

for i in range(len(data)):
    my_dict[data[i]]=my_dict.get(data[i],0)+1
    print(my_dict)  

  