from os import environ, getenv
from pathlib import Path

import uvicorn

HERE = Path(__file__).parent

if __name__ == "__main__":
    if not getenv("LOGURU_LEVEL"):
        environ["LOGURU_LEVEL"] = "DEBUG"

    uvicorn.run("app:app", access_log=False, port=8000, reload=True)