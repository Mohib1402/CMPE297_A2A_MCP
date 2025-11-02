from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
import logging, json

app = FastAPI(title="exchange-mcp", version="0.1.0")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("exchange-mcp")

RATES = {
    "latest": {
        "USD": {"EUR": 0.92, "INR": 83.0, "USD": 1.0},
        "EUR": {"USD": 1.087, "INR": 90.1, "EUR": 1.0},
        "INR": {"USD": 0.012, "EUR": 0.011, "INR": 1.0},
    }
}

class RateResponse(BaseModel):
    base: str = Field(..., examples=["USD"])
    quote: str = Field(..., examples=["EUR"])
    date: str = Field(..., examples=["latest"])
    rate: float = Field(..., examples=[0.92])

@app.get("/healthz")
def healthz():
    return {"ok": True}

def _norm_ccy(x: str) -> str:
    if not x or len(x) != 3 or not x.isalpha():
        raise HTTPException(status_code=400, detail="Currency codes must be 3 letters.")
    return x.upper()

@app.get("/api/get_exchange_rate", response_model=RateResponse)
async def get_exchange_rate(base: str = Query(...), quote: str = Query(...), date: str = Query("latest")):
    base = _norm_ccy(base)
    quote = _norm_ccy(quote)
    day = (date or "latest").lower()
    if day not in RATES:
        day = "latest"
    rate = RATES.get(day, {}).get(base, {}).get(quote)
    log.info("request=%s", json.dumps({"base": base, "quote": quote, "date": day}))
    if rate is None:
        raise HTTPException(status_code=404, detail=f"Rate {base}->{quote} not found for {day}")
    resp = {"base": base, "quote": quote, "date": day, "rate": rate}
    log.info("response=%s", json.dumps(resp))
    return resp