import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Example
if __name__ == '__main__':
    install('pandas')
    install('requests')
    install('install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib')
