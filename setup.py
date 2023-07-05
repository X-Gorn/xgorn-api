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

import re
from setuptools import setup, find_packages


with open('xgorn_api/__init__.py', encoding='utf-8') as f:
    version = re.findall(r'__version__ = \'(.+)\'', f.read())[0]


with open('xgorn_api/api.py', encoding='utf-8') as f:
    base_url = re.findall(r'self\.base_url = \'(.+)\'', f.read())[0]
    base_url_ = base_url.replace("https://", "")


with open('README.md', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='xgorn-api',
    version=version,
    description=f'API Interface for {base_url_}',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/X-Gorn/xgorn-api',
    author='xgorn',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='api scraper bypasser translator client library python',
    project_urls={
        'Web': base_url,
        'Documentation': base_url+'/docs'
    },
    python_requires='~=3.7',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
)