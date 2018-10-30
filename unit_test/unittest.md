# USEFUL PYTEST INFORMATION


## Unit-test Intro
- dev 


## PYTEST Intro
- dev 


```python 

import pytest 

def mytest():
	x = 7 
	assert x ==0 
	

```


## fixture scope 

```python 

@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('-----------------')

```

- function：run every test once. defailt : function scope
- class： run all test once in the class 
- module：run all test once in the module  
- session：only run each session once



## ref 






