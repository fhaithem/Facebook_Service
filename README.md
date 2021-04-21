### Author : Haithem FRAD
### Email : fhaithem533007@gmail.com

A python service that web scrapes the content from facebook using fastAPI. The driver containing specific functions to scrape specific content from facebook :
- Scrapes the user information, profile details
- Scrapes events details
- Scrapes followers details
- Scrapes likes details
- Scrapes photos details

# Prerequisites
```bash
1) Install google chrome
2) Install chromedriver specific for your operating system and chrome version
3) Place the chromedriver executable file the folder
```

# Installation Windows
```bash
1) In the path containing setup.py execute the command to build the package: python setup.py sdist bdist
2) In the same path, execute the command to install the Insta_driver: pip install .
3) Install the required python packages: pip install -r requirements.txt
```
# Install google chrome and chromedriver in linux:
```
# Set the Chrome repo
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
# Install Chrome
apt-get update && apt-get -y install google-chrome-stable
# install chromedriver
apt-get install -y unzip
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
```
```
Install from the server
pip install --user --index-url http://kaisens:Kaizendata.2017@46.105.104.225:8880/simple/ --trusted-host 46.105.104.225 Insta_driver
```
