import requests
from bs4 import BeautifulSoup
import json

def getLinkedInPost(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        script_content = soup.find("script",{"type":"application/ld+json"})
        script_content = script_content.text
        # Parse the JSON data within the script tag
        data = json.loads(script_content)
        post = dict()
        post['schema'] = data
        # Extract information from the JSON data
        post['schemaType'] = data['@type']
        post['text'] = data['articleBody']
        post['image_url'] = data['image']['url'] or None

        return post
    except:
        print("Error")