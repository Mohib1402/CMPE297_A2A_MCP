import os
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI(title="MCP Currency Server")

# Simple in-memory rates for the codelab
RATES = {
    ("USD","EUR"): 0.92, ("EUR","USD"): 1.087,
    ("INR","USD"): 0.012, ("USD","INR"): 83.0,
}

class RateResponse(BaseModel):
    base: str
    quote: str
    date: str
    rate: float

def _norm(c: str) -> str:
    c = (c or "").upper()
    if not (len(c) == 3 and c.isalpha()):
        raise HTTPException(status_code=400, detail="Invalid currency code")
    return c

@app.get("/exchange", response_model=RateResponse)
def exchange(
    base: str = Query(..., description="Base currency (e.g., USD)"),
    quote: str = Query(..., description="Quote currency (e.g., EUR)"),
    date: str = Query("latest", description="Date string or 'latest'"),
):
    b = _norm(base); q = _norm(quote)
    if b == q:
        return RateResponse(base=b, quote=q, date=date, rate=1.0)
    key = (b, q)
    if key not in RATES:
        raise HTTPException(status_code=404, detail=f"Rate {b}->{q} not found for {date}")
    return RateResponse(base=b, quote=q, date=date, rate=RATES[key])
