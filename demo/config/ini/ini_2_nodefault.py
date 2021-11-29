from configparser import ConfigParser

# https://stackoverflow.com/questions/51659954/configparser-missingsectionheadererror-file-contains-no-section-headers/70134461
parser = ConfigParser()
with open('config_nodefault.ini') as stream:
    parser.read_string('[default]\n' + stream.read())

print(parser.get('default', 'username'))

default = parser['default']
print(default.get('email', 'default@email.com'))
