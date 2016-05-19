import pandas as pd

df = pd.read_csv("LangID-JFTokens_Annotation2.csv") #the whole dataframe of csv file is stored in variable df


df2 = df[['language_prediction', 'text']] # df2 variable has just the two columns that we require

df3 = df2.head(100)
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
            sentence =  new_tag + ' :'+ ' '.join(new_list)
            print sentence + '\n'
            new_list = []
            new_tag = df3_list[i][0]
            new_list.append(df3_list[i][1][1:-1])
        
        
    


