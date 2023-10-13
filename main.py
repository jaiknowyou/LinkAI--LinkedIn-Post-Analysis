# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, Response, json
from linkedIn import getLinkedInPost
from openAI import analyze_linkedin_post

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World'
 
@app.route('/insight-LinkedInPost', methods = ['POST'])
def insightLinkedInPost():
    try:
        linkedIn = getLinkedInPost(request.form['url'])
        OpenAIResponse = analyze_linkedin_post(linkedIn['text'])

        return Response(
            response=json.dumps({
                "data": {
                    "schema": linkedIn['schema'],
                    "schemaType": linkedIn['schemaType'],
                    "text": linkedIn['text'],
                    "image_url": linkedIn['image_url'],
                    "OpenAIResponse": OpenAIResponse
                }
            }),
            status=201,
            mimetype="application/json"
        )
    except:
        print("Error")
        return Response("Wait... The API is in repair")

# main driver function
if __name__ == '__main__':
    app.run()