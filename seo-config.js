#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// 页面SEO配置
const seoConfig = {
  'index.html': {
    title: 'MapForVPN - 专业机场测评与VPN推荐 | 2026年最新科学上网指南',
    description: '提供真实的机场测评、VPN推荐和科学上网教程。覆盖速度测试、稳定性分析、流媒体解锁测试，帮你找到最适合的翻墙工具。包含ChatGPT、Netflix、TikTok专用机场推荐。',
    keywords: '机场推荐,VPN推荐,科学上网,翻墙工具,机场测评,VPN测评,梯子推荐,代理服务,ChatGPT机场,Netflix机场',
    ogType: 'website'
  },
  'rankings.html': {
    title: '2026年机场推荐榜单 - 速度与稳定性综合评测 | MapForVPN',
    description: '基于真实测试数据的机场排名榜单，包含速度测试、稳定性评分、价格对比。涵盖高端IPLC专线、性价比中端机场、入门级便宜机场推荐。',
    keywords: '机场榜单,机场排名,机场推荐,VPN排名,最快机场,稳定机场,便宜机场,性价比机场',
    ogType: 'website'
  },
  'reviews.html': {
    title: '机场深度评测 - 云图、极速Cloud、大鸽云全面对比 | MapForVPN',
    description: '专业机场评测文章，包含云图机场、极速Cloud、大鸽云等主流服务商的速度测试、流媒体解锁、节点质量分析。提供机场选择指南和避坑建议。',
    keywords: '机场评测,VPN评测,云图机场,极速Cloud,大鸽云,机场对比,机场选择指南',
    ogType: 'website'
  },
  'wiki.html': {
    title: '科学上网百科 - VPN、Shadowsocks、V2Ray知识全解析 | MapForVPN',
    description: '科学上网科普百科，详解VPN、Shadowsocks、V2Ray、Trojan等协议原理，以及SSR、IPLC、CN2等专业术语，帮助新手快速入门。',
    keywords: '科学上网,VPN原理,Shadowsocks,V2Ray,Trojan,SSR,IPLC,CN2,科学上网百科',
    ogType: 'website'
  },
  'tutorials.html': {
    title: 'VPN使用教程 - Windows/Mac/iOS/Android全平台配置指南 | MapForVPN',
    description: '详细的VPN和机场使用教程，涵盖Clash、V2Ray、Shadowrocket等主流客户端在Windows、Mac、iOS、Android平台的配置方法。',
    keywords: 'VPN教程,Clash教程,V2Ray教程,Shadowrocket教程,科学上网教程,翻墙教程,代理配置',
    ogType: 'website'
  },
  'download.html': {
    title: 'VPN客户端下载 - Clash/V2Ray/Shadowrocket官方版本 | MapForVPN',
    description: '提供Clash、V2RayN、Shadowrocket、QuantumultX等主流VPN客户端的官方下载链接和安装教程，支持Windows、Mac、iOS、Android全平台。',
    keywords: 'VPN下载,Clash下载,V2Ray下载,Shadowrocket下载,客户端下载,翻墙软件下载',
    ogType: 'website'
  },
  'review-yuntu.html': {
    title: '云图机场评测：金融级专线体验 | 930Mbps速度 99.7%稳定性',
    description: '云图机场深度评测：平均速度930Mbps，稳定性99.7%，支持Netflix/Disney+解锁。IPLC专线节点，晚高峰不降速，适合追求极致体验的用户。',
    keywords: '云图机场,云图机场评测,IPLC专线,高速机场,稳定机场,Netflix解锁',
    ogType: 'article'
  },
  'review-jisucloud.html': {
    title: '极速Cloud评测：流媒体解锁专家 | 支持30+平台4K播放',
    description: '极速Cloud机场评测：专注流媒体解锁，支持Netflix、Disney+、HBO Max等30+平台。平均速度885Mbps，4K视频流畅播放，流媒体用户首选。',
    keywords: '极速Cloud,极速Cloud评测,流媒体解锁,Netflix机场,Disney+解锁,4K视频',
    ogType: 'article'
  },
  'review-dageyun.html': {
    title: '大鸽云评测：高性价比入门之选 | 月付¥15起 760Mbps速度',
    description: '大鸽云机场评测：月付仅¥15起，平均速度760Mbps，稳定性99.2%。适合预算有限的学生党和入门用户，性价比极高的机场推荐。',
    keywords: '大鸽云,大鸽云评测,便宜机场,性价比机场,学生机场,入门机场,15元机场',
    ogType: 'article'
  },
  'review-netflix.html': {
    title: '流媒体解锁专题：2026年最佳Netflix机场推荐 | 10家对比测试',
    description: '测试10家主流机场的Netflix、Disney+、HBO Max解锁能力，推荐5家解锁最稳定的机场。包含ChatGPT、TikTok等平台支持情况。',
    keywords: 'Netflix机场,流媒体解锁,Disney+解锁,HBO Max,ChatGPT机场,TikTok解锁',
    ogType: 'article'
  },
  'review-avoid-scams.html': {
    title: '机场避坑指南：识别跑路机场的9大红旗信号 | 2026最新',
    description: '总结机场选择时的9大红旗警示：虚假宣传、只收长期付款、数据安全隐患等。通过真实跑路案例分析，帮你避开骗子机场，保护资金安全。',
    keywords: '机场避坑,跑路机场,机场骗局,机场安全,机场选择,机场红旗',
    ogType: 'article'
  }
};

// 生成SEO meta标签
function generateSEOTags(filename) {
  const config = seoConfig[filename] || {
    title: 'MapForVPN - 专业机场测评与推荐',
    description: '提供真实的机场测评和科学上网教程',
    keywords: '机场推荐,VPN推荐,科学上网',
    ogType: 'website'
  };

  const baseUrl = 'https://mapforvpn.com'; // 替换为实际域名

  return `
    <!-- SEO Meta Tags -->
    <meta name="description" content="${config.description}">
    <meta name="keywords" content="${config.keywords}">
    <meta name="author" content="MapForVPN">
    <meta name="robots" content="index, follow">
    <meta name="googlebot" content="index, follow">
    <meta name="bingbot" content="index, follow">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="${config.ogType}">
    <meta property="og:url" content="${baseUrl}/${filename}">
    <meta property="og:title" content="${config.title}">
    <meta property="og:description" content="${config.description}">
    <meta property="og:site_name" content="MapForVPN">
    <meta property="og:locale" content="zh_CN">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="${baseUrl}/${filename}">
    <meta name="twitter:title" content="${config.title}">
    <meta name="twitter:description" content="${config.description}">

    <!-- Canonical URL -->
    <link rel="canonical" href="${baseUrl}/${filename}">

    <!-- Language -->
    <link rel="alternate" hreflang="zh-CN" href="${baseUrl}/${filename}">
    <link rel="alternate" hreflang="zh" href="${baseUrl}/${filename}">`;
}

// 生成结构化数据
function generateStructuredData(filename) {
  const config = seoConfig[filename];
  if (!config) return '';

  const baseUrl = 'https://mapforvpn.com';

  if (config.ogType === 'article') {
    return `
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "${config.title}",
      "description": "${config.description}",
      "author": {
        "@type": "Organization",
        "name": "MapForVPN"
      },
      "publisher": {
        "@type": "Organization",
        "name": "MapForVPN",
        "logo": {
          "@type": "ImageObject",
          "url": "${baseUrl}/logo.png"
        }
      },
      "datePublished": "2026-08-28",
      "dateModified": "2026-08-28",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "${baseUrl}/${filename}"
      }
    }
    </script>`;
  } else {
    return `
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "MapForVPN",
      "url": "${baseUrl}",
      "description": "${config.description}",
      "publisher": {
        "@type": "Organization",
        "name": "MapForVPN"
      }
    }
    </script>`;
  }
}

console.log('SEO配置已准备完成');
console.log('主要页面数量:', Object.keys(seoConfig).length);
