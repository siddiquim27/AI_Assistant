#https://www.google.com/search?q=weather+of+nagpur
# user_agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
# class = 

from requests_html import HTMLSession
import speech_to_text


s = HTMLSession()
query = 'nagpur'
url = f'https://www.google.com/search?q=weather+of+nagpur'
r = s.get(url, header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})
