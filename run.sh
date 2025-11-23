#!/bin/bash
if pgrep -f "uvicorn main:app" > /dev/null; then
    echo "服务已经在运行中"
    exit 1
fi

# 创建日志文件（如果不存在）
touch log.txt

# 启动FastAPI服务并将日志输出到log.txt，后台运行
nohup uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 > log.txt 2>&1 &

echo "服务已在后台启动，PID: $!"
echo "日志输出到 log.txt"
echo "使用 'tail -f log.txt' 查看实时日志"
echo "使用 'kill $!' 停止服务"