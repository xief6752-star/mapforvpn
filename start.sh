#!/bin/bash

# 机场导航系统 - 本地服务器启动脚本

PORT=8080

echo "🚀 启动机场导航系统..."
echo ""
echo "📍 访问地址："
echo "   主页: http://localhost:$PORT"
echo "   地图: http://localhost:$PORT/china-province-airports.html"
echo "   管理: http://localhost:$PORT/airport-admin.html"
echo ""
echo "💡 按 Ctrl+C 停止服务器"
echo ""

# 检测可用的 HTTP 服务器
if command -v python3 &> /dev/null; then
    echo "✓ 使用 Python3 启动服务器..."
    python3 -m http.server $PORT
elif command -v python &> /dev/null; then
    echo "✓ 使用 Python 启动服务器..."
    python -m SimpleHTTPServer $PORT
elif command -v php &> /dev/null; then
    echo "✓ 使用 PHP 启动服务器..."
    php -S localhost:$PORT
else
    echo "❌ 未找到可用的 HTTP 服务器"
    echo ""
    echo "请安装以下任一工具："
    echo "  - Python 3: brew install python3"
    echo "  - Node.js: brew install node (然后运行 npx serve)"
    echo "  - PHP: brew install php"
    exit 1
fi
