import openai
openai.api_key='------------------------'
img_response = openai.Image.create(
  prompt="a redbull flying with wings flying in blue sky",
  n=2,
  size="1024x1024"
)
image_url = img_response['data'][0]['url']
print(image_url)
