import pandas as pd
import math
import time
start_time = time.time()

pos_file = open('TaggerCodes.csv', 'r+')




myfile = open('final_file.txt', 'wb')

df = pd.read_csv("LangID-JFTokens_Annotation2.csv") #the whole dataframe of csv file is stored in variable df

total_rows=len(df.axes[0])

df2 = df[['language_prediction', 'text']] # df2 variable has just the two columns that we require

df3 = df2.head(total_rows) # df3 has two columns and all rows of respective columns

df3_list = df3.values.tolist() # converting the data frame to list, i.e. list of list

my_list = []
my_dict = {}

new_tag = df3_list [1][0]
print "first post printing:"
index = 0 #initialized the index to keep track of the index

eng_count = 0
eng_count_rev = 0
swahi_count_rev = 0

swahi_count = 0
once_happened = False

    

def first_feature(index):
    temp_tag = df3_list[index][0]
    if temp_tag == 'en':
        return 1
    elif temp_tag == 'sw':
        return 0
    elif temp_tag == 'punc':
        return 4
    elif temp_tag == 'mixed':
        return 2

def second_feature(index):
    if 'Post:' in df3_list[index - 1][1]:
        return -1 # -1 for init
    elif df3_list[index - 1][0] == 'punc':
        temp_tag =  df3_list[index-2][0]
        if temp_tag == 'en':
            return 1
        elif temp_tag == 'sw':
            return 0
        elif temp_tag == 'mixed':
            return 2
        else:
            return 4
    else:
        temp_tag =  df3_list[index-1][0]
        if temp_tag == 'en':
            return 1
        elif temp_tag == 'sw':
            return 0
        elif temp_tag == 'mixed':
            return 2
        else:
            return 4

def third_feature(index): # check two previous words
    if 'Post:' in df3_list[index - 1][1] or 'Post:' in df3_list[index-2][1]:
        return -1 #'init'
    elif df3_list[index -2][0] == 'punc':
        temp_tag = df3_list[index-3][0]
        if temp_tag == 'en':
            return 1
        elif temp_tag == 'sw':
            return 0
        elif temp_tag == 'mixed':
            return 2
        else:
            return 4

    else:
        
        temp_tag = df3_list[index - 2][0]
        if temp_tag == 'en':
            return 1
        elif temp_tag == 'sw':
            return 0
        elif temp_tag == 'mixed':
            return 2
        else:
            return 4

def fourth_feature(index): #looks weather the previous word was same or not
    if 'Post:' in df3_list[index - 1][1]:
        return -1#'init'
    elif second_feature(index) == df3_list[index][0]:
        return 1 #'same'
    else:
        return 0 #'different'

 

def fifth_feature(index): #looks whether the two step previous word was same or not
    if 'Post:' in df3_list[index - 1][1] or 'Post:' in df3_list[index-2][1]:
        return -1 #'init'
    elif third_feature(index) == df3_list[index][0]:
        return 1 #'same'
    else:
        return 0 #'different'

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
    elif df3_list[i][0] == 'mixed':
        return 1
    
    
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
    elif df3_list[i][0] == 'mixed':
        return 0


    


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
    
    
    


for i in range(len(df3_list)-1): #looping through each of the rows
    # First check if the row iterator is pointing to post or not?
    if 'Post:' not in df3_list[i][1] and (i != total_rows or i!= total_rows-1):
        if new_tag == df3_list[i][0] or df3_list[i][0] == 'punc': #if the previous and current word are of same language
            #my_list.append(df3_list[i][1][1:-1])    #appending all the word of same language and punctuation following in a same list
            sixth_feat_val = sixth_feature(swahi_count, eng_count)
            seventh_feat_val = seventh_feature(swahi_count_rev, eng_count_rev)
            temp_value_pos = pos_file.readline().split(',')[1]
            
            #myfile.write(',')
            myfile.write(df3_list[i][1][1:-1])
            myfile.write(',')
            myfile.write(str(temp_value_pos))
            myfile.write(',')
            myfile.write( str(first_feature(index)))
            myfile.write(',')
            
            myfile.write( str( second_feature(index)))
            myfile.write(',')
            myfile.write( str(third_feature(index)))
            myfile.write(',')
            myfile.write( str (fourth_feature(index)))
            myfile.write(',')
            myfile.write( str (fifth_feature(index)))
            myfile.write(',')
            myfile.write( str (sixth_feat_val))
            myfile.write(',')
            myfile.write( str (math.log((sixth_feat_val+ 1), 2)))
            myfile.write(',')
            myfile.write( str (seventh_feat_val))
            myfile.write(',')
            myfile.write( str (math.log((seventh_feat_val+ 1), 2)))
            myfile.write(',')
            myfile.write(  str (sixth_feat_val/(float (sixth_feat_val+ seventh_feat_val))))
            myfile.write(',')
            myfile.write(  str (switch_happened(index)))
            myfile.write(',')
            myfile.write(  str (class_function(index)))            
            myfile.write('\r\n')
                
            #print '..........................................................'

        else:  #if the current word is of not the same language as of previous word
            #print new_tag+ ": ", ' '.join(my_list) # print the previous list as string
            #print '......................................................'
            
            #my_list = []  # reinitializing my_list as a empty list          
            new_tag = df3_list[i][0]
            #my_list.append(df3_list[i][1][1:-1])
            
            #printing the word itself

            
            sixth_feat_val = sixth_feature(swahi_count, eng_count)
            seventh_feat_val = seventh_feature(swahi_count_rev, eng_count_rev)
            
            
            temp_value_pos = pos_file.readline().split(',')[1]
            
            #myfile.write(',')
            myfile.write(df3_list[i][1][1:-1])
            myfile.write(',')
            myfile.write(str(temp_value_pos))
            myfile.write(',')
            myfile.write( str(first_feature(index)))
            myfile.write(',')
            
            myfile.write( str( second_feature(index)))
            myfile.write(',')
            myfile.write( str(third_feature(index)))
            myfile.write(',')
            myfile.write( str (fourth_feature(index)))
            myfile.write(',')
            myfile.write( str (fifth_feature(index)))
            myfile.write(',')
            myfile.write( str (sixth_feat_val))
            myfile.write(',')
            myfile.write( str (math.log((sixth_feat_val+ 1), 2)))
            myfile.write(',')
            myfile.write( str (seventh_feat_val))
            myfile.write(',')
            myfile.write( str (math.log((seventh_feat_val+ 1), 2)))
            myfile.write(',')
            myfile.write(  str (sixth_feat_val/(float (sixth_feat_val+ seventh_feat_val))))
            myfile.write(',')
            myfile.write(  str (switch_happened(index)))
            myfile.write(',')
            myfile.write(  str (class_function(index)))
            
            myfile.write('\r\n')

            
            '''
            print 'word itself: ', df3_list[index][1][1:-1]
            
            print '..........................................................'
        
            vector_list = []

            
            
            #vector_list.append(df3_list[index][1][1:-1])
            
            sixth_feat_val = sixth_feature(swahi_count, eng_count)
            seventh_feat_val = seventh_feature(swahi_count_rev, eng_count_rev)
            vector_list.append(first_feature(index))
            vector_list.append( second_feature(index))
            vector_list.append( third_feature(index))
            vector_list.append( fourth_feature(index))
            vector_list.append( fifth_feature(index))
            vector_list.append( sixth_feat_val)
            vector_list.append( math.log((sixth_feat_val+ 1), 2))
            vector_list.append( seventh_feat_val)
            vector_list.append( math.log((seventh_feat_val+ 1), 2))
            vector_list.append(  sixth_feat_val/(float (sixth_feat_val+ seventh_feat_val)))
            vector_list.append( switch_happened(index))
            vector_list.append( class_function(index))
            for i in vector_list:
                my_file.write(str(i))
                my_file.write(',')
            my_file.write('\n')
           ''' 



    else: #if post is in the row
        if i != 0 :
            #print new_tag + ": ", ' '.join(my_list) #print the previous list as a string
            #my_list =[] # reinitializing my_list as a empty list
            #print '......................................................'
            myfile.write('\r\n')
            myfile.write("new post printing:")
            myfile.write('\r\n')
            swahi_count *= 0
            eng_count *= 0
            swahi_count_rev *= 0
            eng_count_rev *= 0
            once_happened = False

            new_tag = df3_list [i+1][0] # the tag for the next row after new post
    index += 1
    

print("--- %s seconds ---" % (time.time() - start_time))
