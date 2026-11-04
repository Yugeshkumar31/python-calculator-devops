import json

from calculator import add, subtract, multiply


def lambda_handler(event, context):

    params = event.get("queryStringParameters") or {}

    operation = params.get("operation")

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply
    }

    if operation not in operations:
        return response(
            400,
            {"error": "Invalid operation. Use add, subtract or multiply"}
        )

    try:
        a = int(params["a"])
        b = int(params["b"])

        result = operations[operation](a, b)

        return response(
            200,
            {
                "operation": operation,
                "a": a,
                "b": b,
                "result": result
            }
        )

    except (KeyError, TypeError, ValueError):
        return response(
            400,
            {"error": "Provide two positive integers"}
        )


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }