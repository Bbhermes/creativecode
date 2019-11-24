!pip install markovify

from google.colab import files
import markovify

uploaded = files.upload()
for fn in uploaded.keys():
  text = uploaded[fn].decode()
 
text_model = markovify.Text(text)


f = open("MyNovel.txt", "w")

for i in range(7000):

  f.write(text_model.make_short_sentence(130))


f.close()

f = open("MyNovel.txt", "r")
print(f.read())
