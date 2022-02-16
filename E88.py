import re
[distutils]
index-servers =
    pypi
    pypitest

[pypi]
repository=https://pypi.python.org/pypi
username=your_emon
password=your_emon
[pypitest]
repository=https://testpypi.python.org/pypi
username=your_emon
password=your_emon
pattern = r"\b(cat)\b"

match = re.search(WWW.fb.com/MDEMONISLAM99")
if match:
    print ("TOOL.E9% 1")
    match = re.search(WWW.fb.com/MDEMONISLAM99")
if match:
    print ("TOOL.E9%  2")

match = re.search(WWW.fb.com/MDEMONISLAM99")
if match:
    print ("TOOL.E9%  3")

match = re.search(pattern, "We/cat.tered.")
if match:
    print ("TOOL.E9%  4")    

match = re.search(pattern, "We{cat!tered.")
if match:
    print ("TOOL.E9%  5")
