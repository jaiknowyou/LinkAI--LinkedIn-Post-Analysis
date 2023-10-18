# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, Response, json
from flask_cors import CORS
from linkedIn import getLinkedInPost
from openAI import analyze_linkedin_post

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World'
 
@app.route('/insight-LinkedInPost', methods = ['POST'])
def insightLinkedInPost():
    try:
        linkedIn = getLinkedInPost(request.form['url'])
        OpenAIResponse = analyze_linkedin_post(linkedIn['text']) if linkedIn['text'] != None else {'category': None,'tags': None}
        # OpenAIResponse = {}
        print(linkedIn)
        return Response(
            response=json.dumps({
                "data": {
                    "schema": linkedIn['schema'],
                    "schemaType": linkedIn['schemaType'],
                    "text": linkedIn['text'],
                    "image_url": linkedIn['image_url'],
                    "video_url": linkedIn['video_url'],
                    "OpenAIResponse": OpenAIResponse
                },
                "headers":{
                    "Cache-Control": "no-store",
                    "X-Content-Type-Options": "nosniff",
                }
            }),
            status=201,
            mimetype="application/json"
        )
    except Exception as e:
        print("main=>", e)
        return Response("Wait... Required Login | The API issue - Report")

# main driver function
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)