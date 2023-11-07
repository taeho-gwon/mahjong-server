from fastapi import FastAPI
from starlette.responses import PlainTextResponse

app = FastAPI(
    title="mahjong be server",
    description="마작 서버",
)


@app.get("/health_check", response_class=PlainTextResponse, include_in_schema=False)
def health_check():
    return "OK"
