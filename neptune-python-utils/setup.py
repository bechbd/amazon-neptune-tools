"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0
"""
from setuptools import setup


setup(
    name='neptune-python-utils',
    author='amazon-neptune',
    author_email='amazon-neptune-pypi@amazon.com',
    description='Python 3 library that simplifies using Gremlin-Python to connect to Amazon Neptune',
    long_description="""neptune-python-utils is a Python 3 library that simplifies using Gremlin-Python to connect to Amazon Neptune. 
    The library makes it easy to configure your driver to support IAM DB Authentication, create sessioned interactions with Neptune, 
    and write data to Amazon Neptune from AWS Glue jobs.""",
    long_description_content_type='text/markdown',
    url='https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils',
    version=1.0,
    keywords = ['neptune', 'gremlin', 'graph database', 'amazon'],
    install_requires=[
        'gremlinpython>=3.5.1',
        'requests',
        'backoff',
        'cchardet',
        'aiodns',
        'idna-ssl'
    ]
)