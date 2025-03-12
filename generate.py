
#### **generate.py**
```python
import random

snippets = [
    "print('Hello, World!')",
    "for i in range(10): print(i)",
    "const name = 'John'; console.log(name);",
    "int x = 5; printf('%d', x);"
]

print(random.choice(snippets))
