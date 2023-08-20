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

class Scrape:
    
    def __init__(self, api):
        self.api = api
    
    def tiktok(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/tiktok', url=url)
    
    def tiktokv2(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/tiktokv2', url=url)
    
    def facebook(self, url: str) -> dict:
        """
        Deprecated in v1.0.4
        """
        return self.api.make_request('post', '/scrape/facebook', url=url, deprecated=True)
    
    def instagram(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/instagram', url=url)
    
    def instagramv2(self, url: str) -> dict:
        """
        Deprecated in v1.0.4
        """
        return self.api.make_request('post', '/scrape/instagramv2', url=url, deprecated=True)

    def twitter(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/twitter', url=url)
    
    def likee(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/likee', url=url)
    
    def pinterest(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/pinterest', url=url)
    
    def pinterestv2(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/pinterestv2', url=url)
    
    def terabox(self, url: str) -> dict:
        """
        Deprecated in v1.0.4
        """
        return self.api.make_request('post', '/scrape/terabox', url=url, deprecated=True)
    
    def gofile(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/gofile', url=url)
    
    def krakenfiles(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/krakenfiles', url=url)
    
    def yifysubtitles(self, imdb_id: str, lang: str) -> dict:
        return self.api.make_request('post', '/scrape/yifysubtitles', imdb_id=imdb_id, lang=lang)
    
    def filelions(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/filelions', url=url)
    
    def streamwish(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/streamwish', url=url)

    def icons8(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/icons8', url=url)
    
    def novelupdates(self, title: str) -> dict:
        """
        Deprecated in v1.0.7
        """
        return self.api.make_request('post', '/scrape/novelupdates', title=title, deprecated=True)
    
    def reddit(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/reddit', url=url)
    
    def proxy(self, type: str) -> dict:
        return self.api.make_request('post', '/scrape/proxy', type=type)
    
    def voe(self, url: str) -> dict:
        return self.api.make_request('post', '/scrape/voe', url=url)