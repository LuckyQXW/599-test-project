# 599-test-project
To set up the project, we need to install some necessary packages.

First of all, create a new conda environment and activate it using:

```
conda create --name 599env python=3.8
conda activate 599env
```

## Chinese to Pinyin model
Setup instructions found in [this repo](https://github.com/hankcs/pyhanlp). Example code snippet see [here](https://blog.csdn.net/Changxing_J/article/details/104699303).

Run the following commands:
```
conda install -c conda-forge openjdk python=3.8 jpype1=0.7.0 -y
pip install pyhanlp
hanlp
```
Once run `hanlp`, it will take a while to download all the data packages.

## OpenAI GPT model
Run the command:
```
pip install openai
```
To get API key, you need to have an OpenAI account that has some available credits, then find it in user settings. See [this](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).

## Flask Python server
Detailed documentation [here](https://flask.palletsprojects.com/en/2.2.x/)

Run the command:
```
pip install Flask
pip install -U flask-cors
```
Note that we are using `flask-cors` to work around the CORS error when running the server and accessing the API locally.

The server has several endpoints, but the most important ones are `get_gpt_story_fake` that uses an already generated file, and `get-gpt-story-with-prompt` will read in some fields from a POST request form body and construct the prompt before querying OpenAI GPT3 API.

## Starting the Server
Run the command
```
flask --app hello run --debug
```
Then open `index.html` in default browser (as a local file, no need to host it on a live server). Press the submit button to get the generated story.

Note that it currently uses the fake endpoint. To actually generate a new story with the given input, change the call from `getFakeStoryWithDelay` to `getStoryWithData` in `script.js` `init` function.