# How I have validated each of the answers
I used grobid to process the pdf to xml tei and then use python to do the tasks
## Task 1 Draw a keyword cloud based on the abstract information
I first selected documents containing abstracts.
I generate the wordclouds executing the python program. To validate I search the biggest words in the wordcloud and count it in the abstract using a text procesing

## Task 2 Create a visualization showing the number of figures per article
After generate the image with python I check that the number of figures per article was right. I have checked this by counting the figures of each item manually.

# Task 3 Create a list of the links found in each paper
After generate the image with python I check that the list of links were right. I have checked this searching the links of each paper using the function ctl F with the parameter http.
