#Approach:
#loop through all the rows
#Check the text field of the file i.e the last column of each row
#If a '#' is found in the beginning of the string then it is a valid word
				#If we find that the word belongs to English language,
						#We concatenate the english words before the current word
						#We write the last Swahili word to the file and re-initialize it ton a empty string
				#If the word is Swahili word,
						#We concatenate all the Swahili word before the current Swahili word
						#We write the last English word to a file and re-initialize it to an empty string
#If it is a post;
	#We write the current post to the file
	#If there a any unempty sentences to be written (in each languages), we write them
#FInally after getting out of the loop we write the last non-empty sentence to the file







import csv
import treetaggerwrapper
output_file = open("Tagger_Output.text",'w')
def write_sw(sw_sentence,post):
	output_file.write(str(post))
	output_file.write("\n")
	output_file.write("\n")
	tagtest_sw = swTagger.tag_text(unicode(sw_sentence))
	output_file.write("Swahili Sentence")
	output_file.write("\n")
	output_file.write(str(tagtest_sw))
	output_file.write("\n")	
	output_file.write("\n")


def write_en(en_sentence,post):
	output_file.write(str(post))
	output_file.write("\n")
	output_file.write("\n")
	tagtest_en = enTagger.tag_text(unicode(en_sentence))
	output_file.write("English Sentence")
	output_file.write("\n")
	output_file.write(str(tagtest_en))
	output_file.write("\n")
	output_file.write("\n")




csvfile = open('/Users/Gauris/Google Drive/Research_Files/LangID-JFTokens_Annotation2.csv', 'rU')
csvreader = csv.reader(csvfile)

tagdir = '/Users/Gauris/Desktop/InformationProcessingLab'
enTagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR=tagdir,TAGOPT='-token -lemma -sgml -quiet -proto -hyphen-heuristics')
swTagger = treetaggerwrapper.TreeTagger(TAGLANG='sw',TAGDIR=tagdir,TAGOPT='-token -lemma -sgml -quiet -proto -hyphen-heuristics')

sw_sentence = ''
en_sentence = ''
post=''

for row in csvreader:
	if row[-1][0]=='#':          
		if row[0][0]=='s':
			if sw_sentence == '':
				sw_sentence= sw_sentence + row[-1][1:-1]
			else:
				sw_sentence = sw_sentence + ' ' + row[-1][1:-1]
			if en_sentence!='':
				write_en(en_sentence,post)
				en_sentence =''

		elif row[0][0]=='e' :
			if en_sentence == '':
				en_sentence = en_sentence + row[-1][1:-1]
			else:

				en_sentence= en_sentence + " " + row[-1][1:-1] 
			if sw_sentence!='':
				write_sw(sw_sentence,post)
				sw_sentence = ''

		elif row[0][0] == 'p':
			if sw_sentence!="":
				sw_sentence = sw_sentence + row[-1][1:-1]
				en_sentence = ""				
			elif en_sentence!="":
				en_sentence = en_sentence + row[-1][1:-1]
				sw_sentence = ""
	elif row[-1][0]=='P' and sw_sentence!='':
		
		write_sw(sw_sentence,post)
		sw_sentence = ''
		post =  row[-1]

	elif row[-1][0]=='P' and en_sentence!='':	
		write_en(en_sentence,post)
		en_sentence =''
		post =  row[-1]
	elif row[-1][0]=='P':
		post =  row[-1]
	


if en_sentence!="":
	write_en(en_sentence,post)
	en_sentence =''
elif sw_sentence!="":
	write_sw(sw_sentence,post)
	sw_sentence=""
