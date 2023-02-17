import openai, sys
prompt = "给我讲一个有关春节和年兽的儿童睡前故事"
openai.api_key = "<API KEY>"

completions = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=3000,
  n=1,
  stop=None,
  temperature=0.9
)

message = completions.choices[0].text
print(message)

with open("story.txt", 'w') as f:
  f.write(message)