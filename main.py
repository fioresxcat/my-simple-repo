import os
import pdb
import uvicorn
from PIL import Image
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/sum")
def compute_sum(a: float = Query(..., description="First number"), b: float = Query(..., description="Second number")):
    result = a + b
    return JSONResponse(content={"sum": result, "name": "Tung"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))