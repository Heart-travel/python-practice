#/usr/bin/python3

word_dict = {}
fout=open("result.txt","w")

def calculate():
    file = open('./samples.txt')
    word = []
    for eachline in file:
        if word:
            word = list(word) + list(eachline.split())
        else:
            word = eachline.split()
        word_only = sorted(list(set(word)))
        print(word_only)
        word_dict.update({num:word.count(num) for num in word_only})
    for(word,number) in word_dict.items():
            fout.write(word+":%d\n"%number)
        #print(word_dict)

    file.close()

if __name__ == '__main__':
    calculate()

