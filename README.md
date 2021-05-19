# About this bot

This bot mixes up talk titles from ALA Annual Conferences 2016, 2017, and 2018. The mash-up titles are composed of two halves, each from a real ALA program talk.

Inspired as a bot for Python for Beginners workshop I'm co-leading at ALAAC 2018. See: https://github.com/MarkEEaton/bot-tutorial-ala 

# Making the bot

## Getting and cleaning data

- I copied and pasted "Program"-tagged talks from the [ALAAC program website](https://www.eventscribe.com/2018/ALA-Annual/agenda.asp?h=Full%20Schedule&BCFO=S|E). I pasted the entire page's content into Excel, which happened to nicely put each part of the talk info onto separate lines: time, title, location, etc. (Along with a bunch of other text which was, for my purposes, junk.) Then I copied/pasted all the text into a .txt file in [BBEdit](https://www.barebones.com/products/bbedit/).
	- At first, I only used 'Program'-type talks from 2018, but there were only ~300, and it didn't seem like enough. So I added talks from 2016 and 2017, too, totalling around 871 talk titles.
- In BBEdit, I used regular expressions in the find/replace window to strip out everything but the talk title. Example: search for `"Location: .*?\n"`, replace with nothing.
- I also used regular expressions to get rid of annoying talk titles, like "ALA Board of Directors I" and talk title parts, like presenter names that somehow got in the titles. 


## Splitting talk titles

- The full talk titles are in **ala\_all-talk-titles.txt**. Note that I've already gone through this file by hand and taken out mistakes, like when a presenter name was included or a weird character was there. I replaced all m-dashes with colons, among other data-cleaning actions. 
- I wrote a Python script, **splitter.py**, that would split titles in two every time it encountered a `:` or `?`, and every time it encountered `at`, `of`, `for`, `on`, and `and`. 
- For example, a talk title like "Library pet days: books for dogs and cats" would get split into these sets: 
	 - Beginners: 
	 	- Library pet days:
	 	- Library pet days: books for 
	 	- Library pet days: books for dogs and
	 - Enders:
	 	- books for dogs and cats
	 	- dogs and cats
	 	- cats
- Having more data makes a more productive bot, or in other words, more data = more possibilities. It doesn't matter if there are duplicates or similar lines in the Beginners and Enders, since the bot's only tweeting one possibility every hour. 
- These were saved as **ala\_beginners.txt** and **ala\_enders.txt** text files. 

## Generating talk titles

- At first, I tried the Markov maker from our [bot tutorial](https://github.com/MarkEEaton/bot-tutorial-ala), but (a) I didn't have enough talk titles for it to generate new things, and (b) it's not super smart and would end titles with "and" and other non-endy words.
- So that's why I split talk titles into beginning and ending halves. My tweet script, **alatweet.py**, chooses a random beginning and ending from **ala\_beginners.txt*** and **ala\_enders.txt** each time it tweets. It's got just enough human language to sound plausible, but the randomness of which halves get matched can bring in the whimsy, or the uncanniness. 
	- If you download **alatweet.py** and try to use it, you'll get an error because you don't have an alacredentials.py file. Check out our [bot tutorial](https://github.com/MarkEEaton/bot-tutorial-ala) for info about setting up a bot with a credentials file.
	- Note that I changed the ACCESS\_TOKEN variables to ACCESS\_KEY for no reason at all. 

### Examples of generated titles

- The People's Incubator: You
- Biggest Bang for Three-Year Data Reflection & Future Activities
- Motivating Library Learners: School Librarians
- Using Predictive Analytics in for Library Programming and Cataloging & Discovery for School Librarians
- The Diagnostics of Wattpad: Programs for Older Adults
- Secrets to Should we be concerned?
- Be Your Own Mentor: Take Control of Collaborations: Success Stories From Those Serving In An Information Desert
- You Can't Stay Neutral on Social Justice
- Beyond the Bots: New Tools for Determining Rights and Reuse Status for Our Digital Collections

(I had to check to see if those last 2 were actual talk titles! They really are mash-ups.)

## To-dos
1. Comb through data and remove more people's names (mostly done)
1. Don't match titles with 2+ colons together 
1. Incorporate more whimsy... Add in like 100 beginning and ending lines from another source? Song titles? 

