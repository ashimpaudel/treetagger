import pandas as pd
import math
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
index = 0 #initialized the index to keep track of the index

eng_count = 0
eng_count_rev = 0
swahi_count_rev = 0

swahi_count = 0
once_happened = False


def first_feature(index):
    return df3_list[index][0]

def second_feature(index):
    if 'Post:' in df3_list[index - 1][1]:
        return 'init'
    elif df3_list[index - 1][0] == 'punc':
        return df3_list[index-2][0]
    else:
        return df3_list[index-1][0]

def third_feature(index): # check two previous words
    if 'Post:' in df3_list[index - 1][1] or 'Post:' in df3_list[index-2][1]:
        return 'init'
    elif df3_list[index -2][0] == 'punc':
        return df3_list[index-3][0]

    else:
        
        return df3_list[index - 2][0]

def fourth_feature(index): #looks weather the previous word was same or not
    if 'Post:' in df3_list[index - 1][1]:
        return 'init'
    elif second_feature(index) == df3_list[index][0]:
        return 'same'
    else:
        return 'different'

 

def fifth_feature(index): #looks whether the two step previous word was same or not
    if 'Post:' in df3_list[index - 1][1] or 'Post:' in df3_list[index-2][1]:
        return 'init'
    elif third_feature(index) == df3_list[index][0]:
        return 'same'
    else:
        return 'different'

def sixth_feature(prev_swahi, prev_english): # this function takes the two parameter which are the previous count of english word and previous count of swahili word
    global swahi_count
    global eng_count
    if df3_list[i][0] == 'punc':
        if df3_list[i-1][0] == 'sw':
            return swahi_count
        else:
            return eng_count
    elif df3_list[i][0] == 'sw':
        swahi_count += 1
        return swahi_count
    elif df3_list[i][0] == 'en':
        eng_count += 1
        return eng_count
    
def seventh_feature(prev_swahi_rev, prev_english_rev): #this feature counts the number of word in dff language as this word...
    global swahi_count_rev
    global eng_count_rev
    if df3_list[i][0] == 'punc':
        if df3_list[i-1][0] == 'sw':
            return swahi_count_rev
        else:
            return eng_count_rev
    elif df3_list[i][0] == 'sw':
        eng_count_rev += 1
        return swahi_count_rev
    elif df3_list[i][0] == 'en':
        swahi_count_rev += 1
        return eng_count_rev


    


# log base2 of sixth feature and seventh feature inside the function or make the list to record this values..
def switch_happened(index): #returns 1 if switch happened before and return 0 if switch does not happens
    global once_happened
    
    if once_happened == True:
        return 1
    else:
        if df3_list[i][0] == df3_list[i-1][0] or df3_list[i][0] == 'punc':
            return 0
        else:
            once_happened = True
            return 1
            
            
        
def class_function(index):
    if df3_list[index][0] == df3_list[index+1][0] or df3_list[index+1][0] == 'punc':
        return 0
    elif df3_list[index][0] == 'punc':
        if df3_list[index - 1][0] == df3_list[index+1][0]: # this checks the tag of one word before punctuation and one word after punctuatio
            return 0
        else:
            return 1
    else:
        return 1
    
    
    


for i in range(len(df3_list)): #looping through each of the rows
    # First check if the row iterator is pointing to post or not?
    if 'Post:' not in df3_list[i][1]:
        if new_tag == df3_list[i][0] or df3_list[i][0] == 'punc': #if the previous and current word are of same language
            my_list.append(df3_list[i][1][1:-1])    #appending all the word of same language and punctuation following in a same list

            
            
            print 'word itself: ', df3_list[index][1][1:-1]
            print 'lang i: ', first_feature(index)
            print 'lang i-1: ' , second_feature(index)
            print 'lang i-2: ', third_feature(index)
            print '1 previous: ' ,fourth_feature(index)
            print '2 previous: ' ,fifth_feature(index)
            print '# of word in same lang of current word: ', sixth_feature(swahi_count, eng_count)
            print 'log2 (#6 + 1)' , math.log((sixth_feature(swahi_count, eng_count)+ 1), 2)
            print '# of word in same lang of different word: ', seventh_feature(swahi_count_rev, eng_count_rev)
            print 'log2 (#7 + 1)' , math.log((seventh_feature(swahi_count_rev, eng_count_rev)+ 1), 2)
            print 'ratio of #6/ (#6 + #7) : ' ,  sixth_feature(swahi_count, eng_count)/(sixth_feature(swahi_count, eng_count)+ seventh_feature(swahi_count_rev, eng_count_rev))
            print 'if any SWITCH happpened before of current word: ', switch_happened(index)
            print 'switch happens or not', class_function(index)
            print '..........................................................'

        else:  #if the current word is of not the same language as of previous word
            #print new_tag+ ": ", ' '.join(my_list) # print the previous list as string
            #print '......................................................'
            my_list = []  # reinitializing my_list as a empty list          
            new_tag = df3_list[i][0]
            my_list.append(df3_list[i][1][1:-1])
            #printing the word itself
            print 'word itself: ', df3_list[index][1][1:-1]
            print 'lang i: ', first_feature(index)
            print 'lang i-1: ' , second_feature(index)
            print 'lang i-2: ', third_feature(index)
            print '1 previous: ' ,fourth_feature(index)
            print '2 previous: ' ,fifth_feature(index)
            print '# of word in same lang of current word: ', sixth_feature(swahi_count, eng_count)
            print 'log2 (#6 + 1)' , math.log((sixth_feature(swahi_count, eng_count)+ 1), 2)
            print '# of word in same lang of different word: ', seventh_feature(swahi_count_rev, eng_count_rev)
            print 'log2 (#7 + 1)' , math.log((seventh_feature(swahi_count_rev, eng_count_rev)+ 1), 2)
            print 'ratio of #6/ (#6 + #7) : ' ,  sixth_feature(swahi_count, eng_count)/(sixth_feature(swahi_count, eng_count)+ seventh_feature(swahi_count_rev, eng_count_rev))
            print 'if any SWITCH happpened before of current word: ', switch_happened(index)
            print 'switch happens or not', class_function(index)
            print '..........................................................'




    else: #if post is in the row
        if i != 0:
            #print new_tag + ": ", ' '.join(my_list) #print the previous list as a string
            my_list =[] # reinitializing my_list as a empty list
            #print '......................................................'
            #print '\n'
            #print "new post printing:"
            swahi_count *= 0
            eng_count *= 0
            swahi_count_rev *= 0
            eng_count_rev *= 0
            once_happened = False

            new_tag = df3_list [i+1][0] # the tag for the next row after new post
    index += 1
    

print("--- %s seconds ---" % (time.time() - start_time))
