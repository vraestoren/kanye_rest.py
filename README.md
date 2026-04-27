# kanye_rest.py
Web-API for [kanye.rest](https://kanye.rest) A free REST API for random Kanye West quotes (Kanye as a Service)

## Example
```python
from kanye_rest import KanyeRest

kanye_rest = KanyeRest()
random_quote = kanye_rest.get_random_quote()
print(random_quote)
```
