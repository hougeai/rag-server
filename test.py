import requests
import json
from core.utils import call_bailian_model

def test_single_query(query):
    """
    测试单个查询
    """
    # url = "http://localhost:8000/kb_search"
    url = "https://wigwfn--8000.app.cloudstudio.work/kb_search"
    
    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps({"query": query})
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"คำถาม: {query}")
            print(f"คำตอบ: {result.get('data', '未找到答案字段')}")
            return result.get('data')
        else:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"错误信息: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("连接失败，请确认服务是否正在运行")
        return None
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return None

if __name__ == "__main__":
    # test_single_query("API聚合平台的介绍")
    result = call_bailian_model("API聚合平台的介绍")
    print(result)