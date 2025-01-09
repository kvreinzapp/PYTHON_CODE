import ex33
from dis import dis

code_obj = compile('''
for number in the_count:
    print(number)
        ''', '<string>', 'exec')
dis(code_obj)
