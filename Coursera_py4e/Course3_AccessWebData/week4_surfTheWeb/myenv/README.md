if we do `pip install BeautifulSoup`, we might disturb the outer thing, 
so we need to create a virtual environment where we could use the outer
python, and install the `BeautifulSoup` in this environment
```python
python3 -m venv myenv
```
- `-m venv` means use the `venv` module
and we use this:
```python
source myenv/bin/activate
```
to activate our environment, we could use `which pip` to see that our 
pip is already replaced by vm version
you could use `deactivate` to cancell it and 
`rm -rf myenv` will delete everything including the stuff we added.

