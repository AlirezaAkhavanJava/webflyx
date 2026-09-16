# Python examples

These small, dependency-free programs are included for practice:

- `ip_country.py [IP_ADDRESS]` looks up an IP address with the public `ipapi.co` service. It defaults to `8.8.8.8`.
- `word_counter.py [TEXT...]` counts words in a sentence.
- `temperature_converter.py VALUE --from-unit {c,f}` converts Celsius and Fahrenheit.

Example:

```bash
python3 python_examples/ip_country.py 8.8.8.8
python3 python_examples/word_counter.py hello hello world
python3 python_examples/temperature_converter.py 25 --from-unit c
```

The IP example requires an internet connection; the other examples run offline.
