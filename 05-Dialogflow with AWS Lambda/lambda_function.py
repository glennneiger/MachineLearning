# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:08:00 2018

@author: ju195
"""

def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow
    import os
        
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =os.environ["key"]

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
        text=texts, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    return response
    

def lambda_handler(event, context):
    
    texts = event['texts']
    session_id = event['session_id']
    project_id = event['project_id']
    language_code = event['language_code']
    
    detect_intent_texts(project_id, session_id, texts, language_code)
          
    return(None)