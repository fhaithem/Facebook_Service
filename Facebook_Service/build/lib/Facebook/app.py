from fastapi import FastAPI
import uvicorn
import os


app = FastAPI()

@app.get ('/user_info')
def user_info():
    return os.system('scrapy crawl facebook_info -o user_info.json')

@app.get ('/photos')
def get_photos():
    return os.system('scrapy crawl facebook_photos -o photos.json')

@app.get ('/followers')
def get_followers():
    return os.system('scrapy crawl facebook_followers -o followers.json')

@app.get ('/events')
def get_events():
    return os.system('scrapy crawl facebook_events -o events.json')

@app.get ('/likes')
def get_likes():
    return os.system('scrapy crawl facebook_likes -o likes.json')



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4200)


