#!/usr/bin/env python2

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'ticketlog')).read()
mystopwords=('Thanks', 'thanks','it','can','wikimedia','the','to', 'my','is',
	     'width','all','I','with','wikimediafoundation','this','a','can','our', 
	     'you','do','foundation','also','https','org','hi','of','be','that','me',
	     'need','into','out','but','and','no','able','if','for','in','have','as',
	     'will','new','i','are','am','email','so','on','or','your','we','from',
	     'which','at','which','would','there','not','thank','what','donate', 
	     'please','http', 'one', 'help', 'them', 'today', 'like','hire', 
	     'make','any', 'WMF', 'get', 'any', 'about','us', 'info','want', 'they',
	     'case','someone', 'issue', 'Best', 'fax','only', 'much','acces', 
	     'next','then', 'been', 'work', 'form', 'don"t','ext','time','wrote', 
	     'off','Fax', 'meeting', 'WWW', 'www', 'Apple','Tech','she','staff', 
	     'other','user', 'home', 'set','who', 'form','log','pm','system', 
	     'complete','com','was', 'time','Subject','wrote','San','CA','support',
	     'Assistant','had','can"t','I"m','room','her','day','log','sent','cell', 
	     'use','Aug','info','Jun','could','thing','minute','manager','an',
	     'sure','Wikipedia','see','setting','take','being','google','access',
	     'Thanks','list','message','single','up','share','every','sum','team',
	     'wiki','freely','some','may','step','just','phone','should','how','through',
	     'think','CA','Date','Best','computer','bit','p','request','most','having'
	     'something','Aug','doc','trying','say','call','while','add','another',
	     'let','when','floor','their','more','week','I"m','don"t','can"t','it"s',
	     'WMF','by','using','probably','I"ll','right','well','desk','because','using',
	     'several','Jun','working','right','now','member','via','usual','come','good',
	     'two',"That's",'I"ve','San','these','give','few','two','change','days','always',
	     'were','already','having','start','password','check','way','mail','fine','name',
	     'Date','reason','Join','card','I"d','foundation','really','we"ll','Sreet',
	     'cannot','office','that','Join','don"t','human','world','knowledge',
	     'know','commitment','Imagine','San','Date','reality','mean','than','receive'
	     'Fransicso','send','move','seem','docs','people','precious','getting','x6788',
	     'where','ideal','reminder','experience','even','lists','attention','follow')
wordcloud = WordCloud(width=1024,height=768,stopwords=mystopwords).generate(text)

# Draw the positioned words to a PNG file.
wordcloud.to_file(path.join(d, 'ticketcloud.png'))
