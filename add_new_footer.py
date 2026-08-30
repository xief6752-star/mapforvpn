#!/usr/bin/env python3
"""
批量添加新版Footer到所有HTML文件
"""

import os
import re

# Footer HTML模板
NEW_FOOTER_HTML = '''
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
</footer>'''

# Footer CSS模板
NEW_FOOTER_CSS = '''
<style>
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
</style>'''

def update_footer(file_path):
    """更新单个HTML文件的Footer"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 判断是否需要相对路径
        is_in_subdir = '../' in file_path or 'nodes/' in file_path

        footer_html = NEW_FOOTER_HTML
        if is_in_subdir:
            # 替换为相对路径
            footer_html = footer_html.replace('href="rankings.html"', 'href="../rankings.html"')
            footer_html = footer_html.replace('href="review-netflix.html"', 'href="../review-netflix.html"')
            footer_html = footer_html.replace('href="tutorials.html"', 'href="../tutorials.html"')
            footer_html = footer_html.replace('href="wiki.html"', 'href="../wiki.html"')
            footer_html = footer_html.replace('href="reviews.html"', 'href="../reviews.html"')
            footer_html = footer_html.replace('href="index.html#about"', 'href="../index.html#about"')

        # 删除旧的footer（如果存在）
        content = re.sub(r'<footer class="footer">.*?</footer>', '', content, flags=re.DOTALL)

        # 删除旧的footer style（如果存在）
        content = re.sub(r'<style>\s*\.footer\s*\{.*?</style>', '', content, flags=re.DOTALL)

        # 在</body>前插入新footer
        if '</body>' in content:
            content = content.replace('</body>', f'{footer_html}\n\n{NEW_FOOTER_CSS}\n\n</body>')
        else:
            print(f"⚠️  No </body> tag found in {file_path}")
            return False

        # 写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {file_path}")
            return True
        else:
            print(f"⏭️  No changes: {file_path}")
            return False

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    print("开始添加新版Footer...\n")

    # 获取所有HTML文件
    html_files = []

    # 根目录的HTML文件
    for file in os.listdir('.'):
        if file.endswith('.html'):
            html_files.append(file)

    # nodes目录的HTML文件
    if os.path.exists('nodes'):
        for file in os.listdir('nodes'):
            if file.endswith('.html'):
                html_files.append(f'nodes/{file}')

    updated_count = 0
    for file_path in sorted(html_files):
        if os.path.exists(file_path):
            if update_footer(file_path):
                updated_count += 1

    print(f"\n完成！更新了 {updated_count} 个文件")

if __name__ == '__main__':
    main()
