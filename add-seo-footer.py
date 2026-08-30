#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

# SEO配置
SEO_CONFIG = {
    'index.html': {
        'title': 'MapForVPN - 专业机场测评与VPN推荐 | 2026年最新科学上网指南',
        'description': '提供真实的机场测评、VPN推荐和科学上网教程。覆盖速度测试、稳定性分析、流媒体解锁测试，帮你找到最适合的翻墙工具。包含ChatGPT、Netflix、TikTok专用机场推荐。',
        'keywords': '机场推荐,VPN推荐,科学上网,翻墙工具,机场测评,VPN测评,梯子推荐,代理服务,ChatGPT机场,Netflix机场',
    },
    'rankings.html': {
        'title': '2026年机场推荐榜单 - 速度与稳定性综合评测 | MapForVPN',
        'description': '基于真实测试数据的机场排名榜单，包含速度测试、稳定性评分、价格对比。涵盖高端IPLC专线、性价比中端机场、入门级便宜机场推荐。',
        'keywords': '机场榜单,机场排名,机场推荐,VPN排名,最快机场,稳定机场,便宜机场,性价比机场',
    },
    'reviews.html': {
        'title': '机场深度评测 - 云图、极速Cloud、大鸽云全面对比 | MapForVPN',
        'description': '专业机场评测文章，包含云图机场、极速Cloud、大鸽云等主流服务商的速度测试、流媒体解锁、节点质量分析。提供机场选择指南和避坑建议。',
        'keywords': '机场评测,VPN评测,云图机场,极速Cloud,大鸽云,机场对比,机场选择指南',
    },
    'wiki.html': {
        'title': '科学上网百科 - VPN、Shadowsocks、V2Ray知识全解析 | MapForVPN',
        'description': '科学上网科普百科，详解VPN、Shadowsocks、V2Ray、Trojan等协议原理，以及SSR、IPLC、CN2等专业术语，帮助新手快速入门。',
        'keywords': '科学上网,VPN原理,Shadowsocks,V2Ray,Trojan,SSR,IPLC,CN2,科学上网百科',
    },
    'tutorials.html': {
        'title': 'VPN使用教程 - Windows/Mac/iOS/Android全平台配置指南 | MapForVPN',
        'description': '详细的VPN和机场使用教程，涵盖Clash、V2Ray、Shadowrocket等主流客户端在Windows、Mac、iOS、Android平台的配置方法。',
        'keywords': 'VPN教程,Clash教程,V2Ray教程,Shadowrocket教程,科学上网教程,翻墙教程,代理配置',
    },
    'download.html': {
        'title': 'VPN客户端下载 - Clash/V2Ray/Shadowrocket官方版本 | MapForVPN',
        'description': '提供Clash、V2RayN、Shadowrocket、QuantumultX等主流VPN客户端的官方下载链接和安装教程，支持Windows、Mac、iOS、Android全平台。',
        'keywords': 'VPN下载,Clash下载,V2Ray下载,Shadowrocket下载,客户端下载,翻墙软件下载',
    },
}

# Footer HTML模板
FOOTER_HTML = '''
<footer class="footer">
  <div class="footer-content">
    <div class="footer-section">
      <div class="footer-brand">
        <div class="footer-logo">
          <span style="font-weight: 900; color: #2d5016;">Map</span><span style="font-weight: 900; color: #5fb878;">For</span><span style="font-weight: 900; color: #2d5016;">VPN</span>
        </div>
        <p class="footer-desc">专注真实机场测评，帮助用户找到最稳定、最高性价比的科学上网工具。数据持续更新，从不接受付费植入。</p>
      </div>
    </div>

    <div class="footer-section">
      <h4>机场推荐</h4>
      <ul class="footer-links">
        <li><a href="rankings.html">综合榜单</a></li>
        <li><a href="rankings.html#speed">横向对比表</a></li>
        <li><a href="review-netflix.html">ChatGPT机场</a></li>
        <li><a href="review-netflix.html">Netflix机场</a></li>
        <li><a href="review-netflix.html">TikTok机场</a></li>
        <li><a href="rankings.html">便宜机场</a></li>
      </ul>
    </div>

    <div class="footer-section">
      <h4>使用教程</h4>
      <ul class="footer-links">
        <li><a href="tutorials.html">Windows教程</a></li>
        <li><a href="tutorials.html">Mac教程</a></li>
        <li><a href="tutorials.html">iOS教程</a></li>
        <li><a href="tutorials.html">Android教程</a></li>
      </ul>
    </div>

    <div class="footer-section">
      <h4>更多</h4>
      <ul class="footer-links">
        <li><a href="wiki.html">科普百科</a></li>
        <li><a href="reviews.html">优惠专区</a></li>
        <li><a href="index.html#about">关于我们</a></li>
        <li><a href="https://t.me/shinhuw" target="_blank" rel="noopener noreferrer">TG频道</a></li>
      </ul>
    </div>
  </div>

  <div class="footer-bottom">
    <div class="footer-disclaimer">
      <p>⚠️ 免责声明：本站所有内容仅供学习与技术研究参考，请遵守所在地区相关法律法规。本站仅链接至联盟推广链接，点击购买后本站获得少量佣金，但不影响购买价格。</p>
    </div>
    <div class="footer-meta">
      <p>© 2026 MapForVPN · 保留所有权利</p>
      <p>📧 联系我们：<a href="https://t.me/shinhuw" target="_blank" rel="noopener noreferrer">@shinhuw</a> · ⭐ <a href="https://github.com/shinhuw" target="_blank" rel="noopener noreferrer">GitHub 数据仓库</a></p>
    </div>
  </div>
</footer>
'''

# Footer CSS样式
FOOTER_CSS = '''
.footer {
  background: var(--surface);
  border-top: 1px solid var(--border);
  margin-top: 80px;
}

.footer-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 60px 24px 40px;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 40px;
}

.footer-section h4 {
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 16px;
}

.footer-brand .footer-logo {
  font-size: 24px;
  margin-bottom: 12px;
  font-family: 'Noto Sans SC', sans-serif;
}

.footer-desc {
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.6;
  max-width: 400px;
}

.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.2s;
}

.footer-links a:hover {
  color: var(--accent);
}

.footer-bottom {
  max-width: 1400px;
  margin: 0 auto;
  padding: 24px 24px 32px;
  border-top: 1px solid var(--border-soft);
}

.footer-disclaimer {
  margin-bottom: 20px;
}

.footer-disclaimer p {
  color: var(--text-faint);
  font-size: 13px;
  line-height: 1.6;
}

.footer-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}

.footer-meta p {
  color: var(--text-muted);
  font-size: 14px;
  margin: 0;
}

.footer-meta a {
  color: var(--accent);
  text-decoration: none;
  transition: color 0.2s;
}

.footer-meta a:hover {
  color: var(--accent-strong);
}

@media (max-width: 1024px) {
  .footer-content {
    grid-template-columns: 1fr 1fr;
    gap: 32px;
  }
}

@media (max-width: 640px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .footer-meta {
    flex-direction: column;
    align-items: flex-start;
  }
}
'''

def generate_seo_tags(filename):
    """生成SEO meta标签"""
    config = SEO_CONFIG.get(filename, {
        'title': 'MapForVPN - 专业机场测评与推荐',
        'description': '提供真实的机场测评和科学上网教程',
        'keywords': '机场推荐,VPN推荐,科学上网',
    })

    base_url = 'https://mapforvpn.com'

    return f'''
    <!-- SEO Meta Tags -->
    <meta name="description" content="{config['description']}">
    <meta name="keywords" content="{config['keywords']}">
    <meta name="author" content="MapForVPN">
    <meta name="robots" content="index, follow">
    <meta name="googlebot" content="index, follow">
    <meta name="bingbot" content="index, follow">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{base_url}/{filename}">
    <meta property="og:title" content="{config['title']}">
    <meta property="og:description" content="{config['description']}">
    <meta property="og:site_name" content="MapForVPN">
    <meta property="og:locale" content="zh_CN">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{base_url}/{filename}">
    <meta name="twitter:title" content="{config['title']}">
    <meta name="twitter:description" content="{config['description']}">

    <!-- Canonical URL -->
    <link rel="canonical" href="{base_url}/{filename}">
'''

def process_html_file(filepath):
    """处理单个HTML文件，添加SEO标签和footer"""
    print(f"处理文件: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)

    # 1. 更新title
    if filename in SEO_CONFIG:
        content = re.sub(
            r'<title>.*?</title>',
            f"<title>{SEO_CONFIG[filename]['title']}</title>",
            content,
            flags=re.DOTALL
        )

    # 2. 在</head>之前添加SEO标签（如果还没有）
    if 'SEO Meta Tags' not in content:
        seo_tags = generate_seo_tags(filename)
        content = content.replace('</head>', f'{seo_tags}\n</head>')

    # 3. 在</style>之前添加footer CSS（如果还没有）
    if '.footer {' not in content:
        # 查找最后一个</style>标签
        last_style_pos = content.rfind('</style>')
        if last_style_pos != -1:
            content = content[:last_style_pos] + '\n' + FOOTER_CSS + '\n' + content[last_style_pos:]

    # 4. 在</body>之前添加footer HTML（如果还没有）
    if '<footer class="footer">' not in content:
        content = content.replace('</body>', f'{FOOTER_HTML}\n</body>')

    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ 完成: {filepath}")

def main():
    # 获取所有HTML文件
    html_dir = Path('/Users/mac/mapvpn')
    html_files = list(html_dir.glob('*.html'))

    # 排除一些不需要处理的文件
    exclude_files = {'footer-template.html', 'simple-test.html'}
    html_files = [f for f in html_files if f.name not in exclude_files]

    print(f"找到 {len(html_files)} 个HTML文件")
    print("开始处理...\n")

    for html_file in html_files:
        try:
            process_html_file(html_file)
        except Exception as e:
            print(f"❌ 处理失败 {html_file}: {e}")

    print(f"\n✓ 全部完成！共处理 {len(html_files)} 个文件")

if __name__ == '__main__':
    main()
