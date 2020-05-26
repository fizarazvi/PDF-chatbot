#!/bin/bash

cd ..
mkdir ThirdPartyData
cd ThirdPartyData
wget http://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B
rm glove.6B