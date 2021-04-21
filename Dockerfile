FROM ubuntu:18.04
USER root


RUN apt-get -y update 
RUN apt install -y python3.8
RUN apt install -y python3-pip 
RUN apt-get upgrade -y python3-pip
RUN apt install -y wget
RUN apt install nano
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:canonical-chromium-builds/stage
RUN apt-get -y update
RUN apt-get install -y chromium-browser 


COPY ./requirements.txt /requirements.txt
COPY ./Facebook_Service /Facebook_Service
COPY ./chromedriver /chromedriver
RUN cp /chromedriver /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver
ENV LANG C.UTF-8
ENV DISPLAY=:99
#pwd- drivers/
ENV PATH "$PATH:$PWD"
#home- root/
ENV PATH "$PATH:$HOME"
#python path
ENV PATH "$PATH:/root/.local/bin"
#ENV PATH "$PATH:~/.local/bin"

RUN pip3 install -r requirements.txt
CMD ["/Facebook_Service/Facebook/app.py"]
ENTRYPOINT ["python3"]
