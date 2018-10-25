import sys

def string_find(str1,sub_string):
    counter = 0
    i=0

    while i<len(str1):

        if str1.find(sub_string,i)>=0:
            i=str1.find(sub_string,i)+1
            counter+=1
        else:
            break
    return counter

if __name__ == "__main__":

    string1 ='ininini'
    s2='ini'

    print(string_find(string1,s2))