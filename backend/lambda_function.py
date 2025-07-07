from typing import Text
import boto3
import json

translate = boto3.client('translate')
comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        text = body.get('text','')
        target_lang = body.get('target_lang', '')

        if not text or not target_lang:
            return{
                'statusCode': 400,
                'body':json.dumps({'error': 'Missing required parameters...'})
            }


        print(f"Text: {text}, Target: {target_lang}")

        source_lang = comprehend.detect_dominant_language(Text=text)['Languages'][0]['LanguageCode']
        print(f"Detected Source Language: {source_lang}")


        translated_text = translate.translate_text(
            Text=text,
            SourceLanguageCode=source_lang,
            TargetLanguageCode=target_lang
        )['TranslatedText']

        return {
            'statusCode': 200,
            'body': json.dumps({
                'translated_text': translated_text,
                'source_lang': source_lang,
                'target_lang': target_lang
                }),
            'headers':{'Content-Type': 'application/json'}
            }
    except Exception as e:
        print("Error: ", str(e)) # Print full error
        return {
            'statusCode' : 500,
            'body': json.dumps({'error': str(e)})

        }



