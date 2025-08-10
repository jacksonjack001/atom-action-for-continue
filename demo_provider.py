"""
这是一个简单的 FastAPI 演示，展示了如何创建一个上下文提供服务。
可以与 "http" 上下文提供者一起使用。
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn
from dataclasses import dataclass


# 定义输入模型
class ContextProviderInput(BaseModel):
    query: str
    fullInput: str


# 模拟数据库结果的数据类
@dataclass
class SearchResult:
    filename: str
    text: str
    score: float


# 创建 FastAPI 应用
app = FastAPI(title="简单上下文提供服务")


# 模拟向量数据库
def mock_vector_search(query: str) -> List[SearchResult]:
    """模拟向量搜索，返回与查询相关的结果"""
    sample_data = [
        SearchResult(
            filename="user_authentication.py",
            text="def authenticate_user(username: str, password: str):\n    # 检查用户凭据\n    if username in user_db and user_db[username] == password:\n        return True\n    return False",
            score=0.92
        ),
        SearchResult(
            filename="data_processing.py",
            text="def process_data(data: List[Dict]):\n    # 处理输入数据\n    results = []\n    for item in data:\n        processed = transform_item(item)\n        results.append(processed)\n    return results",
            score=0.85
        ),
        SearchResult(
            filename="config.json",
            text='{\n    "api_version": "v1",\n    "max_connections": 100,\n    "timeout": 30,\n    "debug_mode": false\n}',
            score=0.78
        )
    ]
    
    # 简单的模拟相关性过滤 - 实际应用中这里会是真正的向量搜索
    if "auth" in query.lower():
        return [sample_data[0]]
    elif "data" in query.lower():
        return [sample_data[1]]
    elif "config" in query.lower():
        return [sample_data[2]]
    else:
        # 默认返回所有结果，按相关性排序
        return sorted(sample_data, key=lambda x: x.score, reverse=True)


@app.post("/retrieve")
async def retrieve_context(item: ContextProviderInput):
    """
    根据查询检索相关上下文
    """
    print(f"收到查询: {item.query}")
    
    # 查询向量数据库（这里使用模拟函数）
    results = mock_vector_search(item.query)
    
    # 构建 Continue 期望的"上下文项"格式
    context_items = []
    for result in results:
        context_items.append({
            "name": result.filename,
            "description": f"相关度: {result.score:.2f}",
            "content": result.text,
        })
    
    print(f"返回 {len(context_items)} 个结果")
    return context_items


@app.get("/")
async def root():
    """服务根路径，返回简单的欢迎信息"""
    return {"message": "上下文提供服务已启动。使用 POST /retrieve 端点进行查询。"}


# 如果直接运行此脚本，启动服务器
if __name__ == "__main__":
    print("启动上下文提供服务...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
