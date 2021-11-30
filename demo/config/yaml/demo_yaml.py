# See
# https://pyyaml.org/wiki/PyYAMLDocumentation
# https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python

import yaml  # pip install PyYAML

with open('config.yaml', 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print('config:', config)

user = config['servers'][0]['github.com']['user']
print('user:', user)


# dumps
with open('config_generated.yaml', 'w') as f:
    yaml.dump(config, f)
