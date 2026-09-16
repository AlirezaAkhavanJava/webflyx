#!/usr/bin/env python3
"""Look up the country for an IP address using ipapi.co."""

from __future__ import annotations

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def country_for_ip(ip_address: str) -> str:
    """Return the country name reported for an IP address."""
    url = f"https://ipapi.co/{ip_address}/json/"
    with urlopen(url, timeout=10) as response:  # noqa: S310 - demo URL is fixed
        data = json.load(response)

    if data.get("error"):
        raise ValueError(data.get("reason", "The IP lookup failed."))
    return data.get("country_name", "Unknown country")


def main() -> None:
    ip_address = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    try:
        print(f"{ip_address} is located in {country_for_ip(ip_address)}.")
    except (HTTPError, URLError, TimeoutError, ValueError) as error:
        print(f"Could not look up {ip_address}: {error}", file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
