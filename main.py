from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml
from src.subbots.subbot import SubBot
from src.masterbot.router import MasterBot

# Khởi tạo FastAPI app
app = FastAPI()

# Load subbots từ config
with open("bots_config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

subbots = {
    bot["name"]: SubBot(bot["name"], bot["data_path"], bot["collection_name"])
    for bot in config["bots"]
}

# Khởi tạo MasterBot
masterbot = MasterBot(subbots)

# Định nghĩa schema cho request
class QueryRequest(BaseModel):
    query: str

# Định nghĩa schema cho response
class QueryResponse(BaseModel):
    response: str
    category: str

# Endpoint xử lý truy vấn
@app.post("/ask", response_model=QueryResponse)
def ask_question(req: QueryRequest):
    try:
        response, category = masterbot.process_query(req.query)
        return {"response": response, "category": category}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
