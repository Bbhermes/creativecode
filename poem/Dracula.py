!pip install markovify

from google.colab import files
import markovify

uploaded = files.upload()
for fn in uploaded.keys():
  text = uploaded[fn].decode()
  
text_model = markovify.Text(text)

for i in range(10):
  print(text_model.make_short_sentence(50))
