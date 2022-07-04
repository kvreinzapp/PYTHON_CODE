#### `""` is not like `''` when you want to print element in dictionary using `f moremat`:
```python
glossary={
    'append':'A method, attach sth of another',
    'del':'A statement, remove some element',
    'title':'A method, convert the 1st character into uppercase'
}

print(f"append:{glossary['append']}")
print(f'append:{glossary['append']}')
```