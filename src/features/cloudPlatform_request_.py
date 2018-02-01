#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:41:39 2018

@author: Huy
"""

# Notice
# Make sure you have these installed
# Run: pip install --upgrade google-cloud-language
# Test
# 
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six
import sys


def entity_sentiment_text(text):
    """Detects entity sentiment in the provided text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    # Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)
    for entity in result.entities:
#        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
#            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
#            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
#            print(u'  Sentiment : {}'.format(mention.sentiment.score))
#            print(u'  Type : {}'.format(mention.type))
#        print(u'Salience: {}'.format(entity.salience))
#        print(u'Sentiment: {}\n'.format(entity.sentiment))

