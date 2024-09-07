from flask import Flask, request, redirect
from bs4 import BeautifulSoup
import requests

app = Flask('')

@app.route('/<id>')
def taiko(id):
    response = requests.get(
        f'https://columbia-makes.jp/taikonotatsujin2024/entry/entries/music_{id}.html'
    )
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        audio_tag = soup.find('audio')
        audio_src = audio_tag['src'] if audio_tag else None
        print(audio_src)
    except:
        return None
    return redirect(f'https://columbia-makes.jp{audio_src}')


def run():
    app.run(host='0.0.0.0', port=8080)


run()
