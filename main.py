from typing import List, Dict, Any, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from core.utils import call_bailian_model

load_dotenv()

class Success(JSONResponse):
    def __init__(
        self,
        code: int = 200,
        msg: Optional[str] = 'OK',
        data: Optional[Any] = None,
        **kwargs,
    ):
        content = {'code': code, 'msg': msg, 'data': data}
        content.update(kwargs)
        super().__init__(content=content, status_code=code)


class Fail(JSONResponse):
    def __init__(
        self,
        code: int = 400,
        msg: Optional[str] = None,
        data: Optional[Any] = None,
        **kwargs,
    ):
        content = {'code': code, 'msg': msg, 'data': data}
        content.update(kwargs)
        super().__init__(content=content, status_code=code)

app = FastAPI()


class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    answer: str


@app.post("/kb_search", response_model=SearchResponse)
async def search(request: SearchRequest):
    """
    基于本地文档内容搜索答案的接口
    """
    try:
        answer = call_bailian_model(request.query)
        return Success(data=answer)
    except Exception as e:
        return Fail(msg=str(e))
def main():
    print("Hello from rag-server!")


if __name__ == "__main__":
    main()
