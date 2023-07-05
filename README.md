# Noid API

```python
from xgorn_api import NoidAPI

api = NoidAPI()
api.api_key = 'your-api-key'

api.bypass.ouo('https://ouo.io/4ZuwGMc')
```

## Examples

##### Change endpoint to api feature.

For example: `/scrape/instagram`

```python
api.scrape.instagram('https://www.instagram.com/reel/CqcUdr-ppgT/?igshid=YmMyMTA2M2Y=')
```

##### Change default api url.

For example: `api.xgorn.eu.org`

```python
api.base_url = 'https://api.xgorn.eu.org'
```

##### Making custom request.

For example: `/scrape/likee`

```python
# GET request
# method & endpoint: default arguments.
method = 'get'
endpoint = '/scrape/likee'
# url: params because it's **kwargs
url = 'https://likee.video/@MEKDede/video/7199606118785777185'
api.make_request(method=method, endpoint=endpoint, url=url)
```

## Installation

```bash
pip3 install xgorn-api
```
