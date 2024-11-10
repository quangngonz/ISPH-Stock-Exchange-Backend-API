from flask import request

def get_param(param_name, default=None):
    value = request.args.get(param_name)
    if value:
        return value
    data = request.get_json(silent=True) or {}
    return data.get(param_name, default)
