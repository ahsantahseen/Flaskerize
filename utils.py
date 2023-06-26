from cerberus import Validator


def validate_json(schema, body):
    v = Validator(schema)
    v.require_all = True
    return v.validate(body)
