

import pandas as pd
import numpy as np
df = pd.read_csv("LangID-JFTokens_Annotation2.csv")
#print df.head()

df2 = df[['language_prediction', 'text']]
df3 = df2.head(200)
print df3
df3_list = df3.values.tolist()
print type(df3_list[0][0])

new_list = []
print len(df3_list)

new_tag = df3_list [1][0]
for i in range(len(df3_list)):
    if 'Post:' in df3_list[i][1]:
        
        print '\n'
        print '\n'
        print 'new_post starting'
    else:
        if df3_list[i][0] == new_tag or df3_list[i][0] == 'punc':
            new_list.append(df3_list[i][1][1:-1])
        else:
            print new_tag + ' :',' '.join(new_list)
            new_list = []
            new_tag = df3_list[i][0]
            new_list.append(df3_list[i][1][1:-1])
        
        
    

#print df2.tail(100)

#applying map function to just get the text without #
            '''

newframe = df['text'].map(lambda x : x[1:-1])
newframe_list =  newframe.values.tolist() #converting dataframe to list

'''
