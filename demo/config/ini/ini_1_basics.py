import configparser

config = configparser.ConfigParser()
config.read('config.ini')
print("sections are:", config.sections())

if 'github.com' in config:
    if 'username' in config['github.com']:
        user = config['github.com']['username']
    else:
        user = config['default']['username']
    print('user:', user)

github = config['github.com']
user = github.get('username', config['default']['username'])
print('user:', user)

port = config['myserver.com'].getint('port', 22)
print('port:', port)
sudo = config['myserver.com'].getboolean('sudo', False)
print('sudo:', sudo)
timeout = config['myserver.com'].getfloat('timeout', 30)
print('timeout:', timeout)



# dumps
with open('config_generated.ini', 'w') as f:
    config.write(f)
