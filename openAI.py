import openai
import os
import re
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

openai.api_key = os.environ.get('API_KEY')

def analyze_linkedin_post(post_text):
    prompt = f"Identify the category and tags for the following LinkedIn post: '{post_text}'"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None
    )
    print(response)
    # Extract the generated response
    generated_text = response.choices[0].text
    # Define regular expressions to match the Category and Tags
    category_pattern = r"Category: (\w+)"
    tags_pattern = r"Tags: (.+)"

    # Use regular expressions to find the matches
    category_match = re.search(category_pattern, generated_text)
    tags_match = re.search(tags_pattern, generated_text)

    # Extract the category and tags if found
    category = category_match.group(1) if category_match else None

    # Extract tags and split them into a list
    tags = tags_match.group(1).split() if tags_match else []

    print("Category:", category)
    print("Tags:", tags)
    return {
        'category': category,
        'tags': tags
    }