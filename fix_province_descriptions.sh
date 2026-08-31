#!/bin/bash

# 广东
sed -i '' 's|<meta name="description" content="广东地区最专业的机场推荐榜单，基于电信、联通、移动三网真实测速数据。提供低延迟游戏加速、4K流畅观看的IPLC/CN2专线节点，适合深圳、广州、东莞用户。">|<meta name="description" content="2026年广东省（深圳、广州、东莞）最佳机场推荐榜单，基于电信、联通、移动三网真实测速数据。提供低延迟IPLC专线和CN2 GIA节点推荐，平均延迟15-20ms，速度800Mbps+。支持4K视频秒开、Netflix/ChatGPT解锁，专为广东用户优化的机场选购指南。">|g' nodes/guangdong.html

# 上海
sed -i '' 's|<meta name="description" content="上海地区最专业的机场推荐榜单，基于电信、联通、移动三网真实测速数据。提供低延迟游戏加速、4K流畅观看的IPLC/CN2专线节点，适合上海本地用户。">|<meta name="description" content="2026年上海市最佳机场推荐榜单，基于电信、联通、移动三网真实测速数据。提供外贸办公、游戏加速、流媒体专用IPLC专线节点推荐，平均延迟18-20ms。覆盖日本、香港、美国等热门地区，支持Netflix/ChatGPT解锁，专为上海商务和家庭用户优化。">|g' nodes/shanghai.html

# 北京
sed -i '' 's|<meta name="description" content="北京地区最专业的机场推荐榜单，基于电信、联通、移动三网真实测速数据。提供低延迟游戏加速、4K流畅观看的IPLC/CN2专线节点，适合北京本地用户。">|<meta name="description" content="2026年北京市最佳机场推荐榜单，基于电信、联通、移动三网真实测速数据。提供IPLC专线节点推荐，平均延迟17-19ms。特别适合敏感时期使用，稳定抗封锁。支持学术研究、企业办公、Netflix/ChatGPT解锁，专为北京用户优化的高稳定性机场。">|g' nodes/beijing.html

echo "✅ 省份页面description已优化"
