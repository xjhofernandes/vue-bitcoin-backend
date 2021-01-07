from service.BitcoinService import BitcoinService
from model.RequestBody import RequestBody
from enums.Enums import Periods
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
bit_service = BitcoinService()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/updateChart/")
async def update_chart(request: RequestBody):
    period_start = Periods[request.period]
    result = bit_service.period_filter(period_start)
    
    return result

@app.post("/updateChartByCalendar/")
async def update_chart_by_calendar(request: RequestBody):
    start = request.date_start
    end = request.date_end
    result = bit_service.calendar_filter(start, end)

    return result