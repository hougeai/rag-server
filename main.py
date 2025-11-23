import requests
from typing import List, Dict, Any, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

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


def read_local_txt_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
        return ""
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return ""


def call_bailian_model(prompt: str, 
                      api_key: str = "sk-42b0ec0e9639427bb97c4f1c5f4e6c18",
                      model: str = "qwen-turbo") -> str:
    
    context = read_local_txt_file("todo.txt")

    BAILIAN_API_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    messages = [{"role": "system", "content": f"请基于上下文，回答问题：{context}"}]

    # 添加当前问题
    messages.append({"role": "user", "content": prompt})

    data = {
        "model": model,
        "input": {"messages": messages},
        "parameters": {"max_tokens": 1024, "temperature": 0.7}
    }

    try:
        response = requests.post(BAILIAN_API_URL, headers=headers, json=data)
        response.raise_for_status()  # 如果请求失败 (如 4xx, 5xx)，则会抛出异常
        result = response.json()

        # 优先检查 choices 字段，这是更现代的API响应格式
        if "output" in result and "choices" in result["output"]:
            choices = result["output"]["choices"]
            if choices and len(choices) > 0:
                return choices[0]["message"]["content"].strip()

        # 其次检查 text 字段，作为备选
        if "output" in result and "text" in result["output"]:
            return result["output"]["text"].strip()

        return "抱歉，无法解析模型响应"
    except requests.exceptions.RequestException as e:
        return f"API调用错误: {str(e)}"
    except Exception as e:
        return f"发生未知错误: {str(e)}"



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
