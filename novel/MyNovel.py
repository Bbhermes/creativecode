!pip install markovify
!pip install weasyprint

from google.colab import files
import markovify
from weasyprint import HTML

novel = ''

uploaded = files.upload()
for fn in uploaded.keys():
  text = uploaded[fn].decode()
 
text_model = markovify.Text(text)


for i in range(7000):

  novel += str(text_model.make_short_sentence(130))

html_template = f"""
<html>
  <head>
  <title>Troll2</title>
  <style>
    body {{
      font-family: "Times New Roman";
    }}
  </style>
  </head>
  <body>
  {novel}
  </body>
</html>
"""

HTML(string=html_template).write_pdf("MyNovel.pdf")
