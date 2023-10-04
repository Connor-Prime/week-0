def hello_name(user_name):
    print("hello_"+user_name+"!")

def first_odds():
    outputstring=""
    for i in range(1,100,2):
        outputstring = outputstring + str(i) + " "
    
    print(outputstring)


# I could go through each item in list
# The sort function is faster.
# I learned this previously.

def max_num_in_list(a_list):
    
    a_list.sort()
    return a_list[-1]

def is_leap_year(year):

    if(year % 4== 0):

        #conditionals for year leaps evey 100 years

        if(year % 100 == 0):
            if(year % 400 != 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print("\n\nQuestion 1 Test:")
hello_name("conor")

print("\n\nQuestion 2 Test:\n")
first_odds()


print("\n\nQuestion 3 Test:\n")

test_list=[1,4,55,7,8,9,2] # Biggest number 55

print(max_num_in_list(test_list)) #expected output: 55

print("\n\nQuestion 4 Tests:\n")

print(is_leap_year(400)) # expected output: False 
print(is_leap_year(100)) # expected output: True 
print(is_leap_year(55)) # expected output: False
print(is_leap_year(80)) # expected output: True