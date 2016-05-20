import pandas as pd

import time
start_time = time.time()




df = pd.read_csv("LangID-JFTokens_Annotation2.csv") #the whole dataframe of csv file is stored in variable df

total_rows=len(df.axes[0])

df2 = df[['language_prediction', 'text']] # df2 variable has just the two columns that we require

df3 = df2.head(total_rows) # df3 has two columns and all rows of respective columns

df3_list = df3.values.tolist() # converting the data frame to list, i.e. list of list

my_list = []
new_tag = df3_list [1][0]
print "first post printing:"

for i in range(len(df3_list)): #looping through each of the rows
    # First check if the row iterator is pointing to post or not?
    if 'Post:' not in df3_list[i][1]:
        if new_tag == df3_list[i][0] or df3_list[i][0] == 'punc': #if the previous and current word are of same language
            my_list.append(df3_list[i][1][1:-1])    #appending all the word of same language and punctuation following in a same list

        else:  #if the current word is of not the same language as of previous word
            print new_tag+ ": ", ' '.join(my_list) # print the previous list as string
            print '......................................................'
            my_list = []  # reinitializing my_list as a empty list          
            new_tag = df3_list[i][0]
            my_list.append(df3_list[i][1][1:-1])
        




    else: #if post is in the row
        if i != 0:
            print new_tag + ": ", ' '.join(my_list) #print the previous list as a string
            my_list =[] # reinitializing my_list as a empty list
            print '......................................................'
            print '\n'
            print "new post printing:"

            new_tag = df3_list [i+1][0] # the tag for the next row after new post
        
            

        

    

print("--- %s seconds ---" % (time.time() - start_time))
