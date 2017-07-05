#/usr/bin/python3
# -*- coding: utf-8 -*-

import re

word_dict = {}
fout=open("result.txt","w")

def calculate():
    file = open('./text.txt')
    '''  ******* DEBUG 1st *******
    word = []
    for eachline in file:
        if word:
            word = list(word) + list(eachline.split())
        else:
            word = eachline.split()
    '''

    ''' ******* DEBUG 2nd *******
    context = file.read()
    print(type(context))
    print(context)

    word_o = context.lower()
    word = re.split(',|\ |\n|\.|\"|!', word_o)
    while '' in word:
        word.remove("")
    print(type(word))
    print(word)
    '''
    word_o = file.read().lower()
    word = re.split(',|\ |\n|\.|\'|\(|\)|\-|\"|!', word_o) # call re.split to add many separator
    while '' in word:                    # delete the null members
        word.remove("")

    '''******* DEBUG 1st *******
    word_s = str(word)
    print(type(word_s))
    print(word_s)
    print(str(word_s))
    print(list(word_s.lower().split()))
    '''

    word_only = sorted(list(set(word))) # delete the duplicated members
    word_dict.update({num : word.count(num) for num in word_only})
    for(word,number) in word_dict.items():
            fout.write(word+":%d\n"%number)
        #print(word_dict)

    file.close()

if __name__ == '__main__':
    calculate()

