# Kahoot-Bot
A simple bot made in python that joins a specified Kahoot game and sits idle(Will implement random question selection at a later date).

# Prerequisites
You must have python 3 installed. It should come pre-installed on linux. If not, use:
>brew install python3
Or:
>apt install python3

For windows users, you can download python [Here](https://www.python.org/downloads/)

You must also have the selenium module installed.
This can be installed with command:
>pip install selenium

If you don't have pip installed, try:
>brew install pip

Or:
>apt install pip

More info about selenium and how to use it [Here](https://www.seleniumhq.org/)

This script uses chrome driver to produce a headless chrome environment. You must put the executable(chromedriver.exe) in you PATH for this script to work. You can download chromedriver.exe [Here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

# Usage
This script will ask you for a game pin upon startup. It will also ask you for a name and number of bots to join.
Lets say you want your name to be "bot". Your name will be:
>bot.(random number)

Alternitavley, if you tell the script to only have one bot join, it will only show your name, without the random numbers.
You can have as many bots join as you want, although it may impact preformance on the system you are running it on. If you leave the field blank, then 50 bots will join.

# Disclamer
This script is very slow. About one bot joins every 10 seconds(May vary depending on system specs). I am working on this issue.
Also, bots will sit idle and they will not answer questions. I am working on implementing a way to make them answer random questions.

# Thank you!
Thank you very much for veiwing this repository. I am new at python, so any help is appreciated.
