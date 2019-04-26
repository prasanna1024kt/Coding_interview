# word = " hi hello world count hi count "
#
# words = word.split(' ')
#
# word_pair = [(x,1) for x in words if x !='']
#
# print(word_pair)

import numpy
import random
data=numpy.zeros((3,3))

# print(numpy.random(100))

#mat = numpy.random((3,3))
print(data)


from google.cloud import Bigquery as bq

conn = bq.client()

project = conn.project_path("project_name")

for table in project("dataset"):
    print(table)













