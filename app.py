from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import sys
import traceback
from api_response import APIResponse
from api import generate_deep_link
import json

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
class Transfer_Information(BaseModel):
    rec_bin: str
    rec_acc_num: str
    amount: str
    msg: str
    send_bin: str
    
@app.post('/generate_deeplink', tags=["generate_deeplink"])
def login_api(input: Transfer_Information):
    try:
        deeplink = generate_deep_link(input.rec_bin, input.rec_acc_num, input.amount, input.msg, input.send_bin)

        return APIResponse.json_format(deeplink)
    except Exception as e:
        response = str(e)
        print(traceback.format_exc())
        print(sys.exc_info()[2])
        return APIResponse.json_format(response)\


@app.get('/banks_list', tags=["bank_list"])
def bank_list():
    try:
        # Load the banks.json file
        with open("banks.json", "r", encoding="utf-8") as file:
            bank_data = json.load(file)
        
        # Extract the list of banks
        bank_list = bank_data.get("data", [])
        
        return APIResponse.json_format(bank_list)
    except Exception as e:
        # Handle and log errors
        error_message = f"Error loading banks list: {str(e)}"
        print(traceback.format_exc())
        return APIResponse.json_format({"error": error_message}, status_code=500)
if __name__ == "__main__":
    uvicorn.run(app ,host='0.0.0.0', port=3000)