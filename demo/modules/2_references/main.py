import config
import changer
import config as baseConfig
from config import globalvar as g  # separate variable --> it's a copy, so changes don't affect it

print('--- step 0 ---')
print(f'config.globalvar: {config.globalvar}')
print(f'baseConfig.globalvar: {baseConfig.globalvar}')
print(f'g: {g}')

print('--- step 1 ---')
config.globalvar = '1'
print(f'config.globalvar: {config.globalvar}')
print(f'baseConfig.globalvar: {baseConfig.globalvar}')
print(f'g: {g}')

print('--- step 2 ---')
baseConfig.globalvar = '2'
print(f'config.globalvar: {config.globalvar}')
print(f'baseConfig.globalvar: {baseConfig.globalvar}')
print(f'g: {g}')


print('--- step 3 ---')
g = '3'
print(f'config.globalvar: {config.globalvar}')
print(f'baseConfig.globalvar: {baseConfig.globalvar}')
print(f'g: {g}')
