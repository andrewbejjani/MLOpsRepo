from fastapi import FastAPI, Query
from Functions import MultFunc
import uvicorn

app = FastAPI()

@app.get("/get-land-price")
async def LandPriceCalculator(
    PricePerM2: float = Query(..., description="The price of a single square meter land in EUR"),
    AreaM2: float = Query(..., description="The total surface area of the land in square meters")
):
    return {"Land Surface Area (m2)": AreaM2, 
            "Price per m2 (EUR)": PricePerM2,
            "Total Land Price (EUR)": MultFunc(x=PricePerM2, y=AreaM2)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Run the application with the following commands:
# poetry shell
# python main.py

# Access the API at:
# http://127.0.0.1:8000/docs

# if running inside Docker, access at:
# http://localhost:8080/docs