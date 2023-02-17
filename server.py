from flask import Flask, jsonify, request
from flask_cors import CORS
from pyhanlp import *
import openai

openai.api_key = "<API KEY>"
Pinyin = JClass("com.hankcs.hanlp.dictionary.py.Pinyin")

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get-gpt-story")
def get_gpt_story():
    prompt = "写一个有关年兽的童话故事\n人物：小明\n关键词：鞭炮，春节，驱赶\n"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens = 3000,
        n=1,
        stop=None,
        temperature=0.9
    )
    message = completions.choices[0].text
    sentences = message.split()
    pinyin_list = []
    sentence_list = []
    for s in sentences:
        pinyin = HanLP.convertToPinyinList(s)
        pinyin_list.append([p.getPinyinWithToneMark() for p in pinyin])
        sentence_list.append(list(s))
    response = {
        "sentences": sentence_list,
        "pinyins": pinyin_list
    }
    response = jsonify(response)
    response.headers.set('Access-Control-Allow-Origin', "*")
    return response


@app.route("/get-gpt-story-fake")
def get_gpt_story_fake():
    with open('story_晓月.txt') as f:
        message = f.read()
    with open('story_晓月_translation.txt') as f:
        translation = f.read()
    sentences = message.split()
    pinyin_list = []
    sentence_list = []
    for s in sentences:
        pinyin = HanLP.convertToPinyinList(s)
        pinyin_list.append([p.getPinyinWithToneMark() for p in pinyin])
        sentence_list.append(list(s))
    response = {
        "sentences": sentence_list,
        "pinyins": pinyin_list,
        "translation": translation
    }
    response = jsonify(response)
    response.headers.set('Access-Control-Allow-Origin', "*")
    return response

@app.route("/get-gpt-story-with-prompt", methods=["POST"])
def get_gpt_story_with_prompt():
    name = request.form['name']
    topic = request.form['topic']
    keywords = request.form['keywords']
    prompt = f'写一个有关{topic}的童话故事\n'
    prompt += f'人物：{name}\n'
    prompt += f'关键词：{keywords}\n'
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens = 3000,
        n=1,
        stop=None,
        temperature=0.9
    )
    message = completions.choices[0].text
    # with open(f'story_{name}.txt', 'w') as f:
    #     f.write(message)
    prompt += message + "\n"
    prompt += "translation to English: \n"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens = 3000,
        n=1,
        stop=None,
        temperature=0.9
    )
    translation = completions.choices[0].text
    # with open(f'story_{name}_translation.txt', 'w') as f:
    #     f.write(translation)
    sentences = message.split()
    pinyin_list = []
    sentence_list = []
    for s in sentences:
        pinyin = HanLP.convertToPinyinList(s)
        pinyin_list.append([p.getPinyinWithToneMark() for p in pinyin])
        sentence_list.append(list(s))
    # with open(f'story_{name}_data.txt', 'a', encoding='utf8') as f:
    #     for p in pinyin_list:
    #         f.write(" ".join(p) + "\n")
    response = {
        "sentences": sentence_list,
        "pinyins": pinyin_list,
        "translation": translation
    }
    response = jsonify(response)
    response.headers.set('Access-Control-Allow-Origin', "*")
    return response
