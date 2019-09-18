# Dracula Poem

This project is a poem generator in Python. To see it run, download the [python script](Dracula.py) and run it with Python or in a notebook. It will require a program called Markovify, so make sure you've installed that first. 

This script assumes that you have a text file that it can take as its input. For my file I used the entire text of the book Dracula, by Bram Stoker. If you want to get poetry resembling mine you should have a text version of it on file too.

What this script will do is read the input file, parse it for parts of speech, then output a stanza of something that hopefully resembles poetry. The poetic quality of that output will vary widely based on the input, but it will always at least somewhat resemble real poetry. 

For this project our main way of completing the assignment was to use a Text blob. However, my classmate Victoria showed me an alternative way to do it that more reliably spits out a stanza of something that is more likely to resemble poetry. This was Markovify. It was extremely useful because it is preprogrammed to grab words that can be grammaticly correct and use them to form sentences. Because of this I think the poetry my program spits out is stronger than what Text blob could have done for me. The fact that I'm taking from Dracula also adds a cool gothic feeling to the words and moods of the poems that are printed.
