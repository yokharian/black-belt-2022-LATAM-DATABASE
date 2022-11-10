from pathlib import Path
from os import environ, getenv

from starlette.middleware.cors import ALL_METHODS

STAGE = getenv("STAGE", "dev").lower()

HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Methods": ", ".join(ALL_METHODS),
    "Access-Control-Allow-Credentials": "true",
}

environ['AWS_DEFAULT_REGION'] = getenv("AWS_DEFAULT_REGION") or 'us-east-1'
HERE = Path(__file__).parent
ROOT = HERE.parent.parent
