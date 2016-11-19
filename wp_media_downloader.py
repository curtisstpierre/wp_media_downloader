import xml.etree.ElementTree as ET
tree = ET.parse('embarquecomapri.wordpress.2016-11-14.post_type-attachment.001.xml')
root = tree.getroot()
for item in root.iter('item'):
    print item[20].text
import requests
for item in root.iter('item'):
    url = item[20].text
    with open(url.split('/')[-1], 'wb') as handle:
        response = requests.get(pic_url, stream=True)
        if not response.ok:
            print response
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
for item in root.iter('item'):
    url = item[20].text
    with open(url.split('/')[-1], 'wb') as handle:
        response = requests.get(url, stream=True)
        if not response.ok:
            print response
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
