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
from .features import Bypass, Scrape, Translate, Music


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
            files = {}
            if kwargs.get('file'):
                files['file'] = open(kwargs['file'], 'rb')
                del kwargs['file']
            return post(self.base_url+endpoint, data=kwargs, files=files).json()
        else:
            return {'error': True, 'message': 'Invalid method'}