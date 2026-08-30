#!/usr/bin/env python3
"""
批量更新所有HTML文件的导航栏，添加省份节点链接
"""

import os
import re

# 需要更新的HTML文件列表
html_files = [
    'rankings.html',
    'reviews.html',
    'wiki.html',
    'tutorials.html',
    'download.html',
    'vpn-speedtest-map.html',
    'review-yuntu.html',
    'review-jisucloud.html',
    'review-dageyun.html',
    'review-comparison.html',
    'review-guide.html',
    'review-node-selection.html',
    'review-netflix.html',
    'review-avoid-scams.html',
    'tutorial-clash-verge.html',
    'tutorial-v2rayn.html',
    'tutorial-shadowrocket.html',
    'tutorial-clash-android.html',
    'tutorial-quantumult-x.html',
    'tutorial-surge-mac.html',
]

# 旧的导航栏模式（不包含省份节点）
old_nav_pattern = r'<a href="(?:\.\.\/)?reviews\.html" class="navbar-link">机场评测</a>\s*<a href="(?:\.\.\/)?wiki\.html" class="navbar-link">科普百科</a>'

# 新的导航栏（包含省份节点）
new_nav_with_nodes = '''<a href="reviews.html" class="navbar-link">机场评测</a>
      <a href="nodes/" class="navbar-link">省份节点</a>
      <a href="wiki.html" class="navbar-link">科普百科</a>'''

new_nav_with_nodes_relative = '''<a href="../reviews.html" class="navbar-link">机场评测</a>
      <a href="../nodes/" class="navbar-link">省份节点</a>
      <a href="../wiki.html" class="navbar-link">科普百科</a>'''

def update_navbar(file_path):
    """更新单个HTML文件的导航栏"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 判断是否需要相对路径（子目录中的文件）
        use_relative = '../' in content and 'navbar-link' in content

        if use_relative:
            # 匹配带有 ../ 的导航
            pattern = r'<a href="\.\.\/reviews\.html" class="navbar-link">机场评测</a>\s*<a href="\.\.\/wiki\.html" class="navbar-link">科普百科</a>'
            content = re.sub(pattern, new_nav_with_nodes_relative, content)
        else:
            # 匹配不带 ../ 的导航
            pattern = r'<a href="reviews\.html" class="navbar-link">机场评测</a>\s*<a href="wiki\.html" class="navbar-link">科普百科</a>'
            content = re.sub(pattern, new_nav_with_nodes, content)

        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {file_path}")
            return True
        else:
            print(f"⏭️  Skipped (no match or already updated): {file_path}")
            return False

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    print("开始更新导航栏...\n")

    updated_count = 0
    skipped_count = 0

    for file_name in html_files:
        if os.path.exists(file_name):
            if update_navbar(file_name):
                updated_count += 1
            else:
                skipped_count += 1
        else:
            print(f"⚠️  File not found: {file_name}")

    print(f"\n完成！")
    print(f"更新: {updated_count} 个文件")
    print(f"跳过: {skipped_count} 个文件")

if __name__ == '__main__':
    main()
