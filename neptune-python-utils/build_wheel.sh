#!/bin/bash -ex

pushd .
sudo pip3 install virtualenv
rm -rf target
rm -rf temp
mkdir target
virtualenv temp --python=python3.8
source temp/bin/activate
pip3 install gremlinpython==3.5.1
pip3 install requests
pip3 install backoff
pip3 install cchardet
pip3 install aiodns
pip3 install idna-ssl
pip3 install wheel setuptools
python3 setup.py sdist bdist_wheel
deactivate
popd
rm -rf temp