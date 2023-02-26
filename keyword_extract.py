# Load packages
import numpy as np
import pandas as pd
import yake
import matplotlib.pyplot as plt

# Load spacy and get text corpus
#import spacy
#import spacy.cli
# spacy.cli.download("en_core_web_lg")
# nlp = spacy.load("en_core_web_lg")
#spacy.cli.download("en_core_web_md")
#nlp = spacy.load('en_core_web_md')

# Set up keyword extractor
kw_extractor = yake.KeywordExtractor()
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 10
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

# Get text
text1 = 'Overall: In the end, Im happy with Webflow. Its an amazing platform for designers, but its definitely not enough for advanced website building. You can use it just for landing pages, personal blogs, portfolios, and local business websites. If you need advanced functionalities you need to hard code them (losing the benefit offered by the platform) or you need to chose a different platform. Pros: The UX of Webflow and its functionalities are perfect for every designer that wants to approach web design. It empowers designers to build award-winning websites with granular control over the final output. The Webflow hosting is blazing fast, the code generated is clean and lightweight, and the CMS functionalities are great. Cons: For a platform so good is incredible how many cons there are with Webflow: - its not GDPR compliant, and they are actively and deliberately ignoring this issue -  it doesnt have a multi-lingual system. You are forced to rely on third-party apps, that add a huge monthly cost for the maintenance of your website - the e-commerce side is incredibly weak compared to other players - the CMS is capped at 10k items. It may seem a lot, but if you automate CMS library enrichment you end up consuming them quickly - every item is capped at 30 custom fields. Again, 30 may seem a big number, but if you used conditional display logic, you can quickly consume those 30 custom fields (and there are other small limitations). Its limiting also for advanced blog structures, like affiliate blogs that need comparison tables. - the general development of the platform is incredibly slow. They havent added relevant features for years! They even removed the client billing features (I wasnt a fan of it, but they said that they removed it so they can focus on more relevant features, while they are not releasing anything!) - some standard components are not accessible according to WCAG, and you have to rebuild them - a lot of basic components are not pre-built, so you have to custom code them Alternatives Considered: Wix Reasons for Choosing Webflow: It let you build websites with a super solid HTML structure Switched From: Divi and WordPress Reasons for Switching to Webflow: Because Webflow offers me much more functionalities and controls on the output.'
text2 = 'Overall: Overall, despite Webflows high cost, I believe its a great option for relatively simple websites that arent too large. If you want to create a large blog or news site, I would suggest Wordpress because you wont have to pay for your site scaling as you would in Webflow. Webflows editor is not very scaleable, but the things you can accomplish with it are pretty advanced if you work hard (for example, I made a tabs section where the tabs were custom SVG shapes - I would not know how to do this in Wordpress). Its by far the most customizable web builder out there. So, if you have a good understanding of HTML and CSS and can translate that to at least figure out Javascript well enough, and if you want to create sites with a wow factor, I recommend Webflow. Pros: Webflow is great for advanced web developers who understand coding on a deep level. Even though they market it as a no code solution, having a deep understanding of coding makes navigating the user interface so much easier and decreases the time required to learn the platform. It has a massive repository of paid templates that are amazing and free cloneables that can be copied and pasted onto your site which are equally amazing. These options can significantly cut development time. Also, Webflow makes it easy to use advanced CSS options like CSS flex or grid. Overall, theres a lot to like about Webflow. Cons: Webflow is very expensive compared to Wordpress and page builders on Wordpress because the costs are often more than you expected. If you are a business who wants to have a blog or news section, youll likely need to pay for their Business plan AND a CMS plan to be able to have the ability to make blog page templates and store blog article content. There are limits to the CMS items you can store, and Webflow will increase pricing tiers on their plans based on large volumes of traffic, so it is definitely one of the most expensive platforms Ive seen. It is not a good option for small businesses. Also, there is a very steep learning curve to using Webflow, but that is mitigated by the excellent learning courses they provide. Switched From: WordPress Reasons for Switching to Webflow: We switched to Webflow for the advanced interactions and customizability of Webflows platform. It is generally more flexible in what you can accomplish than WordPress because you can do almost anything with simple code or by using user created cloneables. With WordPress, you need to potentially add plugin after plugin to achieve what you want.'

# Extract keywords
topkws = {0:[], 1:[]}
for i,text in enumerate([text1,text2]):
  keywords = custom_kw_extractor.extract_keywords(text)
  topkws[i] = [k[0] for k in keywords]

for i in keywords:
    print(str(i))
print(topkws)

# Group keywords by similarity
#for w1 in topkws[0]:
#  for w2 in topkws[1]:
#    print(w1+'+'+w2+'\n'+str(nlp(w1).similarity(nlp(w2))))

# Search for similar keyword to given keyword
#fkeyw = 'cms'
#for i,text in enumerate([text1,text2]):
#  keywords = custom_kw_extractor.extract_keywords(text)
#  for keyw in keywords:
#    similarity = nlp(fkeyw).similarity(nlp(keyw[0]))
#    if similarity > 0.5:
#      print('Text '+str(i)+', keyword "'+keyw+'": '+str(similarity))

#nlp('cms').similarity(nlp('CMS'))