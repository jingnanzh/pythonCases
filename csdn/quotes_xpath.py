# 2020/20/31

'''
    use XPATH to get top 10 quotes from http://quotes.toscrape.com
'''

# install lxml module

from urllib.request import urlopen
from lxml import etree

url = "http://quotes.toscrape.com"
response = urlopen(url)

# Etree
my_quotes_tree = etree.HTML(response.read().decode("UTF-8"))
print(my_quotes_tree)

list = {}
# copy xpath from website element
span10 = my_quotes_tree.xpath("/html/body/div/div[2]/div[1]/div/span[1]")
author10 = my_quotes_tree.xpath('/html/body/div/div[2]/div[1]/div/span[2]/small')
# print(len(span10))
# print(len(author10))

i=0
for span in span10:
    list[span.text] = author10[i].text
    i+=1

print(list)


#
# for span in span10:
#     print(span.text)
#
#
# print(",".join([x.text for x in author10]))


