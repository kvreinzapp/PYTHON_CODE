from dis import dis

code_obj = compile('''
i = 0
while i < 6:
    i  = i + 1
''', '<string>', 'exec')
dis(code_obj)
