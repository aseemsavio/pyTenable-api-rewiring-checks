# pyTenable-api-rewiring-checks

This repository contains checks for pyTenable-supported, rewired Tenable API endpoints.

## How to run the checks

1. Install the packages in the `requirements.txt`.
2. Include your `Access` and `Secret` key for your Tenable.IO account in the `checks/__init__.py` file.
3. From the root of the project, run the following command.

```
pytest .
```

## Note to contributors

1. Ensure to remove the `Access` and `Secret` keys from the `checks/__init__.py` file before pushing the changes.
2. Add new files containing checks under the `checks` package.
