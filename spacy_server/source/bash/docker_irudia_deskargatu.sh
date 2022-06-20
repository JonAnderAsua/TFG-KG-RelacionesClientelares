#!/bin/bash
sudo docker pull neelkamath/spacy-server:2-en_core_web_sm-sense2vec
sudo docker run --rm -p 8000:8000 neelkamath/spacy-server:2-en_core_web_sm-sense2vec