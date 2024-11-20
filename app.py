from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import sys
import traceback
from api_response import APIResponse
from api import generate_deep_link
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
        return APIResponse.json_format(response)
    
if __name__ == "__main__":
    uvicorn.run(app ,host='0.0.0.0', port=3000)