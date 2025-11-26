# api/utils.py


def safe_cast(type_fn: callable, x: any, default=None) -> any:
    try:
        return type_fn(x)
    except ValueError:
        return default
