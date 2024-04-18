# SUPER HERO STORY !
Ever felt you were destined for great things ?
Run this application to find out who you were meant to be as a super hero!

## This repo contains the following ...
- main.py : A simple python random generator script that creates a super hero and a villain persona with some extra code to display a small window with a button using tkinter. More about tkinter here : [Tk](https://docs.python.org/3/library/tkinter.html)
- pre-commit : To help keep my code clean on commit ! Fot more info read:[Pre-commit](https://pre-commit.com/)
- .github/workflows/actions.yml : Nothing is complete without a good CI pipeline and here I've used none other than GHA (git hub actions)
    - The actions run another iteration of linting.
    - It then creates a PR to my master (deploy) branch ( because I'm too lazy to :D )
    - Once done, it creates a new docker image and pushes it to my very own docker registry (where all my images are stored)
- dockerfile : Why keep it simple, when we can over-complicate stuff ( lolz :D *Disclaimer:This is not how I operate at work* )
    - You guessed it ! This dockerfile is created to help run this wonderful application in a containerized environment.
- Requirements.txt : Has requirements (*libraries/modules needed by the app*).

## How to run this ??
PS : This was deveopled on MacOs (run on windows at your own discretion)

- Fork this repository and clone it to your local machine !
- To run locally:
    - Run `pip install --upgrade pip && pip install -r requirements.txt`.
    - Then, in terminal type `python main.py`

- To run using docker :
- Open iterm and run :
    - `open -a Xquartz`| Wondering what xquartz is, I got you covered! [Xquartz](https://www.xquartz.org/)
    - On another tab, run `/opt/X11/bin/Xquartz :0 -listen tcp` *This will start XQuarts in listen mode*
    - Go back to your first tab & cd into the cloned folder.
    - Run `pip install --upgrade pip && pip install -r requirements.txt`.
    - Run `xhost +localhost` *Allow connections from localhost*
    - Then have docker run the application for you locally using : `docker run -e DISPLAY=docker.for.mac.host.internal:0 docker.io/latest_image_name.`

## Addtional requirements:
- Docker installed locally . You can download it [here](https://docs.docker.com/get-docker/).
- If running with docker, make sure that you have XQuartz installed. (mentioned above)


Et! Voila !!

Enjoy ! I hope this was a fun read  :)
