# 项目概述

基于FastAPI构建的知识问答服务，能够基于本地文档内容回答用户问题。项目集成了阿里云百炼大模型API，提供了/kb_search接口供外部调用。

# 环境准备
```
pip install uv

uv sync

source .venv/bin/activate
```

# 项目结构

```
.
├── main.py              # 主应用文件，包含FastAPI应用和服务逻辑
├── test.py              # 测试脚本，用于测试kb_search接口
├── todo.md              # 项目开发待办事项和进度说明
├── pyproject.toml       # 项目配置和依赖声明
├── README.md            # 项目说明文档
└── run.sh               # 应用启动脚本
```