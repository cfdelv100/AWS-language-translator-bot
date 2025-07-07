import lambda_function

def test_lambda_handler():
    event = {
        'body': '{"text": "Hello World", "target_lang": "es"}'
    }
    response = lambda_function.lambda_handler(event, None)
    assert response['statusCode'] == 200
