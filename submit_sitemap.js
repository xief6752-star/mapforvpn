const https = require('https');
const http = require('http');

const SITE_URL = 'https://mapforvpn.com';
const SITEMAP_URL = `${SITE_URL}/sitemap.xml`;

// 搜索引擎 Ping 端点
const searchEngines = [
  {
    name: 'Google',
    url: `https://www.google.com/ping?sitemap=${encodeURIComponent(SITEMAP_URL)}`
  },
  {
    name: 'Bing',
    url: `https://www.bing.com/ping?sitemap=${encodeURIComponent(SITEMAP_URL)}`
  }
];

// 提交sitemap到单个搜索引擎
function submitSitemap(engine) {
  return new Promise((resolve, reject) => {
    console.log(`\n正在提交到 ${engine.name}...`);
    console.log(`URL: ${engine.url}`);

    https.get(engine.url, (res) => {
      console.log(`${engine.name} 响应状态码: ${res.statusCode}`);

      res.on('data', (chunk) => {
        console.log(`${engine.name} 响应: ${chunk}`);
      });

      res.on('end', () => {
        if (res.statusCode === 200) {
          console.log(`✅ ${engine.name} 提交成功`);
          resolve();
        } else {
          console.log(`⚠️ ${engine.name} 提交状态码: ${res.statusCode}`);
          resolve(); // 不reject，继续提交其他引擎
        }
      });
    }).on('error', (err) => {
      console.error(`❌ ${engine.name} 提交失败: ${err.message}`);
      resolve(); // 不reject，继续提交其他引擎
    });
  });
}

// 提交到所有搜索引擎
async function submitToAllEngines() {
  console.log('========================================');
  console.log('开始提交 Sitemap 到搜索引擎');
  console.log(`Sitemap URL: ${SITEMAP_URL}`);
  console.log('========================================');

  for (const engine of searchEngines) {
    await submitSitemap(engine);
  }

  console.log('\n========================================');
  console.log('✅ Sitemap 提交完成！');
  console.log('========================================');
}

// 执行
submitToAllEngines().catch(err => {
  console.error('提交过程出错:', err);
  process.exit(1);
});
