# SEO 提交指南

## 自动提交（已完成）

### IndexNow 提交
已通过 `submit_indexnow.js` 自动提交到 Bing 和其他支持 IndexNow 的搜索引擎。

```bash
node submit_indexnow.js
```

**状态**: ✅ 已提交 18 个主要页面
**响应**: 202 Accepted（已接受）

---

## 手动提交（推荐）

### 1. Google Search Console
1. 访问: https://search.google.com/search-console
2. 添加网站验证
3. 在左侧菜单选择 "站点地图"
4. 提交: `https://mapforvpn.com/sitemap.xml`

### 2. Bing Webmaster Tools
1. 访问: https://www.bing.com/webmasters
2. 添加网站验证
3. 在左侧菜单选择 "站点地图"
4. 提交: `https://mapforvpn.com/sitemap.xml`

### 3. 百度搜索资源平台
1. 访问: https://ziyuan.baidu.com
2. 添加网站验证
3. 在"数据引入" → "链接提交"
4. 提交: `https://mapforvpn.com/sitemap.xml`

---

## IndexNow 密钥

**Key**: `c93e75ba82fc24da07a5f7a17108a2fd`

**验证文件位置**:
- `/indexnow-key.txt`
- `/c93e75ba82fc24da07a5f7a17108a2fd.txt`

两个文件都包含相同的密钥内容，用于搜索引擎验证。

---

## 已提交的页面

### 主要页面 (6个)
- 首页
- 机场榜单
- 机场评测
- 志愿者招募
- 科普百科
- 使用教程

### 省份节点 (4个)
- 省份导航页
- 广东节点
- 上海节点
- 北京节点

### 评测文章 (8个)
- 云图机场评测
- 极速Cloud评测
- 大哥云评测
- 机场横向对比
- 机场选购指南
- 节点选择指南
- Netflix机场推荐
- 防骗避坑指南

---

## 定期更新

每次网站内容更新后，运行以下命令通知搜索引擎：

```bash
node submit_indexnow.js
```

这会自动通知 Bing、Yandex 等支持 IndexNow 的搜索引擎。

---

## 验证状态

### IndexNow
- ✅ 已提交成功（状态码 202）
- 搜索引擎将在后台处理索引

### Google / Bing
- ⏳ 需要在各自的 Webmaster 控制台手动提交和验证

---

## 注意事项

1. **robots.txt** 已配置，允许所有搜索引擎抓取
2. **sitemap.xml** 包含所有重要页面，每周更新频率
3. **IndexNow key** 文件需要保持在网站根目录
4. 每次添加新页面后，记得：
   - 更新 `sitemap.xml`
   - 运行 `submit_indexnow.js`
   - 在 Search Console 重新提交 sitemap

---

## 联系方式

如有问题，联系 TG: @shinhuw
