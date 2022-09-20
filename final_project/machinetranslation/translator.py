"""
translator.py
This module contains the functions for translating english phrases into french and viceverse.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

#Take environment variables from .env
load_dotenv()

apikey = os.environ['api_key']
url = os.environ['url'] 

#Create a authenticator implementation for IAM with the required properties.
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-09-16',
    authenticator=authenticator
)

#Set the language translator service base URL, that corresponds to the location service instance.
language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translate english text input into french."""
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text
    

def french_to_english(french_text):
    """Translate french text input into english."""
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text
