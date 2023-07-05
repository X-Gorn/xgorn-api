#  MIT License

#  Copyright (c) 2023 X-Noid

#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:

#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from requests import get, post


class NoidAPI:
    
    def __init__(self) -> None:
        self.bypass = Bypass(self)
        self.scrape = Scrape(self)
        self.translate = Translate(self)
        self.music = Music(self)
        self.api_key = 'api-key'
        self.base_url = 'https://api.xgorn.pp.ua'
    
    def make_request(self, method: str, endpoint: str, **kwargs) -> dict:
        kwargs['api_key'] = self.api_key
        if self.api_key == 'api-key':
            return {'error': True, 'message': 'Invalid API key'}
        if method == 'get':
            return get(self.base_url+endpoint, params=kwargs).json()
        elif method == 'post':
            return post(self.base_url+endpoint, data=kwargs).json()
        else:
            return {'error': True, 'message': 'Invalid method'}
    
class Bypass:
    
    def __init__(self, api):
        self.api = api
    
    def ouo(self, url: str) -> dict:
        return self.api.make_request('get', '/bypass/ouo', url=url)
    
    def mirrored(self, url: str, host: str) -> dict:
        return self.api.make_request('get', '/bypass/mirrored', url=url, host=host)

class Scrape:
    
    def __init__(self, api):
        self.api = api
    
    def tiktok(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/tiktok', url=url)
    
    def facebook(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/facebook', url=url)
    
    def instagram(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/instagram', url=url)
    
    def instagramv2(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/instagramv2', url=url)

    def twitter(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/twitter', url=url)
    
    def twitterv2(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/twitterv2', url=url)
    
    def likee(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/likee', url=url)
    
    def pinterest(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/pinterest', url=url)
    
    def pinterestv2(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/pinterestv2', url=url)
    
    def terabox(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/terabox', url=url)
    
    def gofile(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/gofile', url=url)
    
    def krakenfiles(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/krakenfiles', url=url)
    
    def yifysubtitles(self, imdb_id: str, lang: str) -> dict:
        return self.api.make_request('get', '/scrape/yifysubtitles', imdb_id=imdb_id, lang=lang)
    
    def filelions(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/filelions', url=url)
    
    def streamwish(self, url: str) -> dict:
        return self.api.make_request('get', '/scrape/streamwish', url=url)

class Translate:
    
    def __init__(self, api):
        self.api = api
    
    def srt(self, url: str, source_lang: str, dest_lang: str) -> dict:
        return self.api.make_request('get', '/translate/srt', url=url, source_lang=source_lang, dest_lang=dest_lang)

class Music:
    
    def __init__(self, api):
        self.api = api
    
    def shazam(self, url: str, type_: str) -> dict:
        return self.api.make_request('get', '/music/shazam', url=url, type=type_)