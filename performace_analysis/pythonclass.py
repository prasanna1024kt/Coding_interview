class pythonclass(object):
    """
    Example for public variable ,
    Python bydefault creates public variables and method we can able to access from even from outside the class

    """

    def __init__(self):
        self.val=None
        self.val2=None

    def value1(self,val):

        self.val=val
        return self.val
    def value2(self,val2):
        self.val2=val2
        return self.val2
cl = pythonclass()
print (cl.val,cl.val2)
cl.val="ptr"
print(cl.val)

print(cl.value1('prasanna'))
print(cl.value2('kumar'))

# Reverse the string sentence using python .

def reverse_word(input_string):


    word = []
    length = len(input_string)
    spaces = [' ']

    i= 0

    while i<length:

        if i not in spaces:
            word_start = i

            while i<length and input_string[i] not in spaces:
                i +=1
            word.append(input_string[word_start:i])
        i +=1
    return " ".join(reversed(word))

s = " my name is you"

print(reverse_word(s))



