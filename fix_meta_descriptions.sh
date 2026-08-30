#!/bin/bash

# 优化各页面的meta description（150-160字符）

# 首页
sed -i '' 's|<meta name="description" content="提供真实的机场测评、VPN推荐和科学上网教程。覆盖速度测试、稳定性分析、流媒体解锁测试，帮你找到最适合的翻墙工具。包含ChatGPT、Netflix、TikTok专用机场推荐。">|<meta name="description" content="MapForVPN提供2026年最新机场测评和VPN推荐。基于真实速度测试、稳定性分析、流媒体解锁验证，帮助用户选择最适合的科学上网工具。覆盖IPLC专线、CN2 GIA、性价比机场推荐，支持ChatGPT、Netflix、TikTok解锁。提供全平台客户端教程和避坑指南。">|g' index.html

# 机场榜单
sed -i '' 's|<meta name="description" content="基于真实测试数据的机场排名榜单，包含速度测试、稳定性评分、价格对比。涵盖高端IPLC专线、性价比中端机场、入门级便宜机场推荐。">|<meta name="description" content="2026年最新机场排名榜单，基于真实速度测试、延迟监控、流媒体解锁能力综合评分。包含云图、极速Cloud、大哥云等主流机场深度对比，涵盖高端IPLC专线、性价比中端机场、入门级便宜机场推荐。提供价格、流量、节点数量、协议支持完整对比表。">|g' rankings.html

# 机场评测
sed -i '' 's|<meta name="description" content="专业机场评测文章，包含云图机场、极速Cloud、大鸽云等主流服务商的速度测试、流媒体解锁、节点质量分析。提供机场选择指南和避坑建议。">|<meta name="description" content="深度机场评测文章集合，涵盖云图机场、极速Cloud、大哥云、寰宇云等主流服务商的真实速度测试、延迟监控、流媒体解锁验证、节点质量分析。提供2026年机场选购指南、避坑建议、节点选择技巧、Netflix/ChatGPT专用机场推荐，帮助用户做出明智选择。">|g' reviews.html

# 下载页面
sed -i '' 's|<meta name="description" content="提供Clash、V2RayN、Shadowrocket、QuantumultX等主流VPN客户端的官方下载链接和安装教程，支持Windows、Mac、iOS、Android全平台。">|<meta name="description" content="提供Clash Verge、V2RayN、Shadowrocket、QuantumultX、Clash for Android等主流代理客户端的官方下载链接和详细安装教程。支持Windows、Mac、iOS、Android全平台，包含客户端功能对比、配置导入教程、常见问题解决方案。">|g' download.html

echo "✅ Meta descriptions 优化完成"
