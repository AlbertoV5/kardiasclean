# Kardiasclean

Clean, Normalize, and Tokenize medical records data.

## Install

```shell
pip install kardiasclean
```

## Usage

```python
import kardiasclean

data['surgery'] = kardiasclean.split_string(data['surgery'])
data_map = kardiasclean.spread_column(data['surgery'])

data_map['surgery'] = kardiasclean.clean_accents(data_map['surgery'])
data_map['surgery'] = kardiasclean.clean_symbols(data_map['surgery'])
data_map['keywords'] = kardiasclean.clean_stopwords(data_map['surgery'])
data_map['token'] = kardiasclean.clean_tokenize(data_map['keywords'])
```

## Development

```shell
poetry run pytest
```

## Changelog

- 0.1.5: Fixes to stopwords implementation, added lowercase conversion.
- 0.1.3: Added Documentation.
- 0.1.2: Added SQL support and improved pre-processing functions.
- 0.1.1: Small readme fixes.
- 0.1.0: Initial Release.