# 项目概述

基于FastAPI构建的知识问答服务，能够基于本地文档内容回答用户问题。项目集成了阿里云百炼大模型API，提供了/kb_search接口供外部调用。

# 环境准备
```
# 准备虚拟环境
pip install uv
uv sync # 安装依赖包
source .venv/bin/activate # 激活虚拟环境

# 准备环境变量：修改.env里的配置项
cp .env.example .env
```

# 项目结构

```
.
├── core # 核心功能模块
│ └── utils.py # 工具函数
├── mcp-server # MCP服务相关文件
│ ├── README.md # MCP服务说明文档
│ ├── calculator.py # 计算器MCP工具示例
│ ├── knowledgebase.py # 知识库MCP工具实现
│ ├── mcp_config.json # MCP配置文件
│ ├── mcp_pipe.py # MCP通信管道
│ └── run.sh # MCP服务启动脚本
├── main.py # 主应用文件，包含FastAPI应用和服务逻辑
├── pyproject.toml # 项目配置和依赖声明
├── README.md # 项目说明文档
├── run.sh # 应用启动脚本
└── test.py # 测试脚本，用于测试kb_search接口
```