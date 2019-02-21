import pandas as pd

bodys = []
dict={}
with open("../mail_sample1.txt","r") as file:
        body = ""
        for line in file:
            if line.startswith("From:"):

                From=line.split("From:")[1].replace('\n','').replace('\r','')
                dict["From"]=From
            elif line.startswith("Sent:"):
                sent=line.split("Sent:")[1].replace('\n','').replace('\r','')
                dict["Sent"] = sent
            elif line.startswith("To:"):
                To=line.split("To:")[1].replace('\n','').replace('\r','')
                dict["To"]=To
            else:
                if line.startswith("From:") or line.startswith("To:") or line.startswith("Sent:"):
                    continue
                if line.startswith("Subject:"):
                    if body != '':
                        continue
                    dict["subject"]=line.split("Subject:")[1].replace('\n','').replace('\r','')
                if not line.startswith("Subject:"):
                    line=line.replace('\n','').replace('\r','')
                    body += line
        dict["body"]=body  # appends the last body of the mail
        body = ""

#print(dict)
df=pd.DataFrame.from_dict(dict,orient='index')
print(df.head())

import sys
ptr_xrange=xrange(0,1000)
print(sys.getsizeof(ptr_xrange))
ptr_range=range(0,1000)
print(sys.getsizeof(ptr_range))