import boto3
import json
import numpy as np
import pandas as pd
import yake
import matplotlib.pyplot as plt

#df = pd.read_excel('/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Trustpilot/Trustpilot-Webflow-filtered.xlsx')
#df = pd.read_excel('/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Trustpilot/Trustpilot-Squarespace-filtered.xlsx')
#df = pd.read_excel('/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Trustpilot/Trustpilot-WIX-filtered.xlsx')
#df = pd.read_excel('/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Capterra/Webflow/Capterra-webflow-filtered.xlsx')
#df = pd.read_excel('/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Capterra/Squarespace/Capterra-squarespace-filtered.xlsx')
df = pd.read_excel('/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Capterra/Wix/Capterra-wix-filtered.xlsx')


# Set up keyword extractor
kw_extractor = yake.KeywordExtractor()
language = "en"
max_ngram_size = 1
deduplication_threshold = 0.8
numOfKeywords = 5
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

# Get text

data_dict = {'keyword 1':[], 'relevance 1':[], 'keyword 2':[],'relevance 2':[], 'keyword 3':[],'relevance 3':[], 'keyword 4':[],'relevance 4':[], 'keyword 5':[],'relevance 5':[]}

print('Calling keywords')

for index, row in df.iterrows():
    
    Text = str(row[0])
    keywords = custom_kw_extractor.extract_keywords(Text)
    count = 1

    if (len(keywords) == 5):

        for i in keywords:
            data_dict['keyword '+ str(count)].append(i[0])
            data_dict['relevance '+ str(count)].append(i[1])

            #print(str(i))
            count = count + 1
        
    elif (len(keywords) == 4):

        for i in keywords:
            data_dict['keyword '+ str(count)].append(i[0])
            data_dict['relevance '+ str(count)].append(i[1])

            #print(str(i))
            count = count + 1
        
        data_dict['keyword 5'].append("")
        data_dict['relevance 5'].append("")

    elif (len(keywords) == 3):

        for i in keywords:
            data_dict['keyword '+ str(count)].append(i[0])
            data_dict['relevance '+ str(count)].append(i[1])

            #print(str(i))
            count = count + 1

        data_dict['keyword 4'].append("")
        data_dict['relevance 4'].append("")        
        data_dict['keyword 5'].append("")
        data_dict['relevance 5'].append("")
    
    elif (len(keywords) == 2):

        for i in keywords:
            data_dict['keyword '+ str(count)].append(i[0])
            data_dict['relevance '+ str(count)].append(i[1])

            #print(str(i))
            count = count + 1

        data_dict['keyword 3'].append("")
        data_dict['relevance 3'].append("")  
        data_dict['keyword 4'].append("")
        data_dict['relevance 4'].append("")        
        data_dict['keyword 5'].append("")
        data_dict['relevance 5'].append("")
    
    elif (len(keywords) == 1):

        for i in keywords:
            data_dict['keyword 1'].append(i[0])
            data_dict['relevance 1'].append(i[1])

            #print(str(i))
        data_dict['keyword 2'].append("")
        data_dict['relevance 2'].append("")        
        data_dict['keyword 3'].append("")
        data_dict['relevance 3'].append("")  
        data_dict['keyword 4'].append("")
        data_dict['relevance 4'].append("")        
        data_dict['keyword 5'].append("")
        data_dict['relevance 5'].append("")

    else:
        data_dict['keyword 1'].append("")
        data_dict['relevance 1'].append("")           
        data_dict['keyword 2'].append("")
        data_dict['relevance 2'].append("")        
        data_dict['keyword 3'].append("")
        data_dict['relevance 3'].append("")  
        data_dict['keyword 4'].append("")
        data_dict['relevance 4'].append("")        
        data_dict['keyword 5'].append("")
        data_dict['relevance 5'].append("")


# Create a dataframe
df1 = pd.DataFrame.from_dict(data_dict)

# Export to Excel
#df1.to_excel('/Users/annijavitolina/Desktop/uni/bachelor/Keywords/Trustpilot-Webflow-keywords.xlsx')
#df1.to_excel('/Users/annijavitolina/Desktop/uni/bachelor/Keywords/Trustpilot-Squarespace-keywords.xlsx')
#df1.to_excel('/Users/annijavitolina/Desktop/uni/bachelor/Keywords/Trustpilot-WIX-keywords.xlsx')
#df1.to_excel('/Users/annijavitolina/Desktop/uni/bachelor/Keywords/Capterra-Webflow-keywords.xlsx')
#df1.to_excel('/Users/annijavitolina/Desktop/uni/bachelor/Keywords/Capterra-Squarespace-keywords.xlsx')
df1.to_excel('/Users/annijavitolina/Desktop/uni/bachelor/Keywords/Capterra-Wix-keywords.xlsx')
