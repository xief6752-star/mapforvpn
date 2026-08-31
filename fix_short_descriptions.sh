#!/bin/bash

# 扩展所有104字符的默认description到140字符
OLD_DESC="MapForVPN提供专业的机场测评和VPN推荐服务。基于电信、联通、移动三网真实测速数据，按省份地区智能推荐最适合本地的机场节点。覆盖速度测试、延迟监控、流媒体解锁验证，帮助用户选择稳定可靠的科学上网工具。"

NEW_DESC="MapForVPN提供专业的机场测评和VPN推荐服务。基于电信、联通、移动三网在全国31省市的真实测速数据，按省份、地区、运营商智能推荐最适合本地的机场节点。覆盖速度测试、延迟监控、稳定性评估、流媒体解锁验证，帮助用户找到性价比最高、最稳定可靠的科学上网工具。"

# 替换所有使用旧默认description的页面
for file in *.html nodes/*.html; do
  if [ -f "$file" ]; then
    if grep -q "$OLD_DESC" "$file"; then
      sed -i '' "s|$OLD_DESC|$NEW_DESC|g" "$file"
      echo "✅ 已扩展: $file"
    fi
  fi
done

echo "========================================="
echo "✅ 所有短description已扩展完成"
echo "========================================="
