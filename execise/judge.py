#!/usr/bin/python3 

def judge(a, b):
    '''
        This function is used for testing if it is sensoring 
        for the sequence between list, tuple and set 
    '''

    if a == b:
        print("for " + "a equals b")
    else:
        print("a doesn't equals b")

if __name__ == '__main__':
    a_list = ["0", "1", "2"]
    b_list = ["1", "0", "2"]
    
    a_tuple = ("0", "1", "2")
    b_tuple = ("1", "0", "2")
    
    a_set = {"0", "1", "2"}
    b_set = {"1", "0", "2"}
 
    type(a_set)
    judge(a_list, b_list)
    judge(a_tuple, b_tuple)
    judge(a_set, b_set)

