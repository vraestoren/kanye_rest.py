<div align="center">
  <img src="https://camo.githubusercontent.com/6dbebc578e6dcce6ca822ef1cce914e5b53d9a27ff3d0c6dc4edc810efa533ef/68747470733a2f2f6b616e79652e726573742f69636f6e2e706e67" width="80" />

# kanye_rest.py

> Web-API for [Kanye Rest](https://kanye.rest) a free REST API for random Kanye West quotes.

</div>

## Quick Start

```python
from kanye_rest import KanyeRest

kanye = KanyeRest()

# Get a random quote
print(kanye.get_random_quote())

# Get a random quote as plain text
print(kanye.get_random_quote_as_text())

# Get all quotes
print(kanye.get_all_quotes())
```

---

<div align="center">

## Quotes

| Method | Description |
|--------|-------------|
| `get_random_quote()` | Get a random Kanye quote as JSON |
| `get_random_quote_as_text()` | Get a random Kanye quote as plain text |
| `get_all_quotes()` | Get the full list of all quotes |

</div>
