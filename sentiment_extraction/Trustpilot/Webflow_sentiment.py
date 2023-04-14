import boto3
import json
import pandas as pd

comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')
df = pd.read_excel('/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Trustpilot/Trustpilot-Webflow-filtered.xlsx')

out_file = open("/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Trustpilot/Webflow/Webflow_sentiment.xlsx", "w")
all_jsns = []

data_dict = {'content-length':[], 'date':[], 'Sentiment':[], 'Mixed':[], 'Negative':[], 'Neutral':[], 'Positive':[]}


for index, row in df.iterrows():
    print(row[0])

    row_str = str(row[0])
    DetectSentimenttext = row_str
    print('Calling DetectSentiment')
    sentiment = json.dumps(comprehend.detect_sentiment(Text=DetectSentimenttext, LanguageCode='en'), sort_keys=True, indent=4)
    print(sentiment)
    print('End of DetectSentiment\n')
    #out_file.write(sentiment)

    sentiment = json.loads(sentiment)
    
    # Put info in dictionary

    data_dict['content-length'].append(sentiment['ResponseMetadata']['HTTPHeaders']['content-length'])
    data_dict['date'].append(sentiment['ResponseMetadata']['HTTPHeaders']['date'])
    data_dict['Sentiment'].append(sentiment['Sentiment'])
    data_dict['Mixed'].append(sentiment['SentimentScore']['Mixed'])
    data_dict['Negative'].append(sentiment['SentimentScore']['Negative'])
    data_dict['Neutral'].append(sentiment['SentimentScore']['Neutral'])
    data_dict['Positive'].append(sentiment['SentimentScore']['Positive'])

    
# Create a dataframe
df1 = pd.DataFrame.from_dict(data_dict)

# Export to Excel
df1.to_excel('/Users/annijavitolina/Desktop/uni/bachelor/Scraped/Trustpilot/Webflow/Webflow_sentiment.xlsx')


