import lambda_function

def test_lambda_handler():
    event = {
        'body': '{"text": "Hello", "target_lang": "fr"}'
    }
    response = lambda_function.lambda_handler(event, None)
    assert response['statusCode'] == 200
