import sys
import re


def validate_user(username, minlen):
    assert type(username) == str, "user must be a string"
    if minlen < 1:
        raise ValueError("Tiene que ser mayor que 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
    

def principal( argv ):
    print(validate_user([], 1))
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi