For my Novel for our NaNoGenMo project I chose to take the script from a movie and generate a novel out of it. The movie I chose was the notoriously bad film from the 1990s called Troll 2.

To create the novel I chose to work with Markovify and Markov chains. I chose Markov chains because they are fmailiar to me. I also used them for our poetry project earlier this year. To get my code to work I used an upload function in python that allows me to upload a text file from my computer to the python script. That text file is included in the novel file here. The text file was a copy of the script to Troll 2.

After that I used the python functions to create a text file named MyNovel.txt. Then I used Markov chains to generate short sentences in the file that will always end up being over 50,000 words long. Here is what that looks like:

f = open("MyNovel.txt", "w")

for i in range(7000):

  f.write(text_model.make_short_sentence(130))
  
After that my novel is generated. I also included a print function so we can see what the novel ends up saying because it will say something different every time.

To create my code I took some of my code from my poem filer here on Github as well as using a tutorial on how to write text files in python. Here is the link for that tutorial:
https://www.geeksforgeeks.org/reading-writing-text-files-python/
