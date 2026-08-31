#!/bin/bash

# 批量优化所有页面的meta description

# 通用的默认description（用于那些只有16字符的页面）
DEFAULT_DESC="MapForVPN提供专业的机场测评和VPN推荐服务。基于电信、联通、移动三网真实测速数据，按省份地区智能推荐最适合本地的机场节点。覆盖速度测试、延迟监控、流媒体解锁验证，帮助用户选择稳定可靠的科学上网工具。"

# 查找所有16字符的description并替换
for file in *.html nodes/*.html; do
  if [ -f "$file" ]; then
    # 检查是否包含16字符的默认description
    if grep -q 'meta name="description" content="提供真实的机场测评和科学上网教程"' "$file"; then
      sed -i '' "s|<meta name=\"description\" content=\"提供真实的机场测评和科学上网教程\">|<meta name=\"description\" content=\"$DEFAULT_DESC\">|g" "$file"
      echo "✅ 已更新: $file"
    fi
  fi
done

# 教程页面 - 更具体的description
sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="详细的代理客户端配置教程，包含Clash Verge、V2RayN、Shadowrocket、QuantumultX等主流客户端的安装、订阅导入、规则配置步骤。支持Windows、Mac、iOS、Android全平台，提供图文教程和常见问题解决方案。">|g' tutorials.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="Clash Verge完整使用教程，包含Windows/Mac版本下载、订阅导入、节点选择、规则配置、TUN模式设置等详细步骤。适合新手的图文教程，帮助快速上手Clash Verge客户端，实现稳定的科学上网。">|g' tutorial-clash-verge.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="V2RayN完整使用教程，包含Windows版本下载、订阅导入、节点测速、路由规则配置等详细步骤。提供V2RayN常见问题解决方案，帮助用户快速上手V2Ray协议客户端，实现高速稳定的网络代理。">|g' tutorial-v2rayn.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="Shadowrocket（小火箭）iOS完整使用教程，包含App Store下载购买、订阅导入、节点配置、规则设置等详细步骤。提供Shadowrocket常见问题解决方案，帮助iPhone/iPad用户快速上手。">|g' tutorial-shadowrocket.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="Clash for Android完整使用教程，包含安卓版本下载、订阅导入、节点选择、规则配置、开机自启等详细步骤。适合Android手机用户的图文教程，帮助快速实现稳定的移动网络代理。">|g' tutorial-clash-android.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="QuantumultX（圈X）iOS完整使用教程，包含App Store购买下载、订阅导入、节点配置、重写规则、策略组设置等高级功能详解。适合进阶iOS用户的专业代理工具配置指南。">|g' tutorial-quantumult-x.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="Surge for Mac完整使用教程，包含Mac版本下载、订阅导入、模块配置、规则编写、网络调试等高级功能详解。适合macOS用户的专业网络代理工具，提供完整的配置指南和优化建议。">|g' tutorial-surge-mac.html

# Wiki百科页面
sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="机场科学上网百科知识库，详解IPLC专线、CN2 GIA、BGP中转等线路类型区别，介绍Shadowsocks、V2Ray、Trojan等协议特点，普及流量倍率、节点选择、DNS泄露等专业术语，帮助用户更好理解机场服务。">|g' wiki.html

# 评测文章
sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="云图机场深度评测，基于真实速度测试、延迟监控、流媒体解锁验证的综合分析。包含节点质量、价格套餐、客服体验、稳定性表现等多维度评分，提供详细的使用建议和购买指南，帮助用户判断是否适合自己。">|g' review-yuntu.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="极速Cloud机场深度评测，基于三网真实测速、节点稳定性、流媒体解锁能力的综合分析。包含CN2 GIA线路质量、价格性价比、TikTok原生IP解锁、客服响应速度等详细测试数据和使用体验分享。">|g' review-jisucloud.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="大哥云机场深度评测，老牌稳定机场的真实测速和使用体验分析。包含节点质量、Netflix/ChatGPT解锁能力、免费试用体验、价格套餐对比、客服支持等多维度评测，提供详细的购买建议。">|g' review-dageyun.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="2026年主流机场横向对比评测，包含云图、极速Cloud、大哥云、寰宇云等热门服务商的速度、延迟、价格、稳定性、流媒体解锁能力全方位对比。提供详细的数据对比表和选购建议，帮助用户找到最适合的机场。">|g' review-comparison.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="机场选购完整指南，从新手到进阶用户的选择建议。详解如何判断线路质量、识别虚假宣传、避免跑路风险、选择合适套餐、测试节点速度等实用技巧。提供机场服务商资质审核要点和避坑清单。">|g' review-guide.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="机场节点选择技巧详解，教你如何根据使用场景挑选最优节点。包含延迟、速度、负载、协议的选择标准，游戏加速、流媒体观看、ChatGPT使用等不同场景的节点推荐，帮助充分发挥机场性能。">|g' review-node-selection.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="Netflix/ChatGPT专用机场推荐榜单，基于真实流媒体解锁测试的精选推荐。包含支持Netflix、Disney+、HBO、ChatGPT、TikTok等服务的机场列表，提供原生IP节点、解锁稳定性、价格对比等详细信息。">|g' review-netflix.html

sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="机场防骗避坑完整指南，识别跑路机场、虚假宣传、钓鱼网站的实用技巧。包含常见骗局案例分析、安全购买建议、退款维权方法、黑名单机场列表等内容，帮助用户避免经济损失和信息泄露风险。">|g' review-avoid-scams.html

# 志愿者招募页面
sed -i '' 's|<meta name="description" content="提供真实的机场测评和科学上网教程">|<meta name="description" content="MapForVPN招募全国各地测速志愿者，提供长期免费高质量IPLC/CN2专线节点作为回报。需要电信、联通、移动三网用户帮助完善省份测速数据，每周2-3次简单测速，获得稳定免费节点长期使用权。">|g' volunteer.html

echo ""
echo "========================================="
echo "✅ 所有meta description已优化完成"
echo "========================================="
