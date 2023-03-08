
import xml.etree.ElementTree as ET
import os
import matplotlib.pyplot as pyplot

from wordcloud import WordCloud, STOPWORDS
from grobid_client.grobid_client import GrobidClient

'''Function to find the links'''
def links(myPath):
    '''Check if the folder exists'''
    if not(os.path.exists(myPath+'/links')):
        os.mkdir(myPath+'/links')

    arrLinks = []

    for xml in os.listdir(myPath+'/xmls'):
        tree = ET.parse(myPath+'/xmls/'+xml)
        root = tree.getroot()
        for element in root.findall('.//{http://www.tei-c.org/ns/1.0}p'):
            text = element.text
            splitText = text.split()
            for word in splitText:
                if 'https://' in word:
                    if word[-1] == '.':
                        new_word = word.replace(word[-1], '')
                        arrLinks.append(new_word)
                    else:
                        arrLinks.append(word)
                        
    content = '\n'.join(arrLinks)
    file = open(myPath+'/links/links.txt', 'w')
    file.writelines(content)


'''Function to create a wordcloud per article'''
def keywordClouds(myPath):

    '''Add words no relevants to stopwords'''

    stopwords = STOPWORDS
    stopwords.add('et')
    stopwords.add('al')


    '''Check if the folder exists if not create one'''

    if not(os.path.exists(myPath+'/wordclouds')):
        os.mkdir(myPath+'/wordclouds')


    '''Loop to create the keyWordcloud'''

    for xml in os.listdir(myPath+'/xmls'):
        tree = ET.parse(myPath+'/xmls/'+xml)
        root = tree.getroot()
        element = root.find('.//{http://www.tei-c.org/ns/1.0}abstract/{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}p')
        text = element.text

        wc = WordCloud(background_color = 'white', stopwords = stopwords, height = 600, width = 600)
        wc.generate(text)
        wc.to_file(myPath+'/wordclouds/'+xml+'_keyword_cloud.png')


'''Function to count a do a plot of the figures per article'''
def figures(myPath):
    y = []
    x = []
    i = 1
    

    if not(os.path.exists(myPath+'/figures')):
        os.mkdir(myPath+'/figures')

    for xml in os.listdir(myPath+'/xmls'):
        tree = ET.parse(myPath+'/xmls/'+xml)
        root = tree.getroot()
        x.append('Paper '+ '\n' +str(i)+'')
        i += 1
        n = 0
        for element in root.findall('.//{http://www.tei-c.org/ns/1.0}figure'):
            n += 1
        y.append(n)

    pyplot.bar(x, y, label = 'Number of Figures')
    pyplot.title('FIGURES PER ARTICLE')
    pyplot.savefig(myPath+'/figures/graphFigures.png')

myPath = os.getcwd()

'''Check if the folder exists'''

if not(os.path.exists(myPath+'/xmls')):
    os.mkdir(myPath+'/xmls')


'''Call the grobid client to process the pdf''' 

client = GrobidClient(config_path='./config.json')
client.process('processFulltextDocument', myPath+'/pdfs', myPath+'/xmls', n=20)


keywordClouds(myPath)
figures(myPath)
links(myPath)
