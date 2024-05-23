import re


def clean_response(chain_response):
    cleaned_response = re.sub(r'`+', '', chain_response).strip()
    cleaned_response = re.sub(r'(sql\s*)+', '', cleaned_response, flags=re.IGNORECASE).strip()
    cleaned_response = re.sub(r'(python\s*)', '', cleaned_response, flags=re.IGNORECASE).strip()
    return cleaned_response


def response_formatting(chain_response):
    if type(chain_response) is str:
        return chain_response
    elif type(chain_response) is dict:
        cleaned_response = clean_response(chain_response['answer'])
        return cleaned_response
