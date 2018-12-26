
def anagram(str1,str2):
    """
    Anagram :
             An anagram is a word or phrase formed by changing the order of the letters in another word or phrase.
             For example, 'triangle' is an anagram of 'integral'.

    :param str1: String 1 value
    :param str2: String 2 value
    :return:
    """
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ', '').lower()

    return sorted(str1) == sorted(str2)

def anagram2(str1,str2):

    #edge cases check for anagram
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    if len(str1) != len(str2):
        return False
    count = {}
    # creating the empty dictionary- to check frequency of each letter in the str
    # for checking the count of each letters in the str1

    for letter in str1:

        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
   # reversing the count of each letter in str in second loop
    for letter in str2 :

        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0 :
            return False
    return True




if __name__ == '__main__':

    print ("exceuting the anagram program solving in one way ")

    s1 = 'dogadv'
    s2 = 'godvda'

    print(anagram(s1,s2))

    print ("exceuting the anagram program solving in second way ")

    print(anagram2(s1, s2))

