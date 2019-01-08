import glob
import os
import re
import pandas as pd
import sys


ncontextlines=3
#sGroup = "Commonrepository"
sGroup = str(sys.argv[1])
sregxcsvFile = "LogAnalysisRegex.csv"
#sFileSearch = "C:\\Prudential\\NSCCFile\\JobLogs\\*.log"
sFileSearch = str(sys.argv[2])

pd.set_option('display.max_colwidth', -1)
dfRegExa =  pd.read_csv(sregxcsvFile)
dfRegExa['Compiled-Regex']=re.compile('')
dfRegExa = dfRegExa.to_dict(orient='records')

dfSearchResults = pd.DataFrame(columns=['Category','Label','LineNo','MatchString','MatchContext','DataCollection'])

print("Searching For")
for iregex in range(dfRegExa.__len__()):
	dfRegExa[iregex]['Compiled-Regex']=re.compile(dfRegExa[iregex]['Reg-Ex'])
	if(sGroup in dfRegExa[iregex]['Category']):
		print(dfRegExa[iregex]['Reg-Ex'])
	
for sfilename in glob.glob(sFileSearch):
	with open(sfilename, "r") as in_file:
		iLineIndex=0
		qcontext = []
		for line in in_file:
			iLineIndex = iLineIndex + 1
			qcontext.append(line)
			if (iLineIndex > ncontextlines):
				qcontext.pop()
			for iregex in range(dfRegExa.__len__()):
				if(sGroup in dfRegExa[iregex]['Category']):
					line_regex = dfRegExa[iregex]['Compiled-Regex']
					mData = line_regex.search(line)
					if (mData):
						sDataMatch= mData.group(0)
						dfSearchResult = pd.DataFrame([[dfRegExa[iregex]['Category'],dfRegExa[iregex]['Label'],iLineIndex,line,qcontext.copy(),sDataMatch]], columns=['Category','Label','LineNo','MatchString','MatchContext','DataCollection'])       
						dfSearchResults = dfSearchResults.append(dfSearchResult)						

#dfSearchResults.to_csv('SearchResult.csv')
dfSearchResults.to_html('SearchResult.html')
print("Matches Found")
dfLabelCount=dfSearchResults.groupby(by='Label', as_index=False).agg({'LineNo': pd.Series.nunique})
dfLabelCount.columns = ['Match Label', 'Number of Matches']
print(dfLabelCount)
#print("Matches Strings {} ".format(dfSearchResults.MatchString))
print(dfSearchResults['MatchContext'])
