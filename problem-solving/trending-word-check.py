stop_word=["is", "an", "a", "the", "of", "that", "this", "i" ]
#
# with open("sampledataset.txt","r") as file_Read:
#
#     word_count={}
#     count=0
#
#     for line in file_Read:
#
#         lines=line.split()
#
#         for word in lines:
#
#             if lines not in word_count:
#
#                    word_count[lines] = 1
#
#             else:
#
#                    word_count[lines] +=1


file=open("sampledataset.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in stop_word:

        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

for k,v in sorted(wordcount.values()):

    print k,v

file.close();
