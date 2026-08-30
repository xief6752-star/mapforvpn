const https = require('https');
const fs = require('fs');

// IndexNow API配置
const INDEXNOW_KEY = fs.readFileSync('indexnow-key.txt', 'utf8').trim();
const SITE_URL = 'https://mapforvpn.com';

// 需要提交的URL列表
const urls = [
  `${SITE_URL}/`,
  `${SITE_URL}/rankings.html`,
  `${SITE_URL}/reviews.html`,
  `${SITE_URL}/volunteer.html`,
  `${SITE_URL}/wiki.html`,
  `${SITE_URL}/tutorials.html`,
  `${SITE_URL}/nodes/`,
  `${SITE_URL}/nodes/guangdong.html`,
  `${SITE_URL}/nodes/shanghai.html`,
  `${SITE_URL}/nodes/beijing.html`,
  // 评测页面
  `${SITE_URL}/review-yuntu.html`,
  `${SITE_URL}/review-jisucloud.html`,
  `${SITE_URL}/review-dageyun.html`,
  `${SITE_URL}/review-comparison.html`,
  `${SITE_URL}/review-guide.html`,
  `${SITE_URL}/review-node-selection.html`,
  `${SITE_URL}/review-netflix.html`,
  `${SITE_URL}/review-avoid-scams.html`,
];

// IndexNow 提交函数
function submitToIndexNow(urlList) {
  const postData = JSON.stringify({
    host: 'mapforvpn.com',
    key: INDEXNOW_KEY,
    keyLocation: `${SITE_URL}/indexnow-key.txt`,
    urlList: urlList
  });

  const options = {
    hostname: 'api.indexnow.org',
    port: 443,
    path: '/indexnow',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(postData)
    }
  };

  const req = https.request(options, (res) => {
    console.log(`状态码: ${res.statusCode}`);
    console.log(`响应头: ${JSON.stringify(res.headers)}`);

    res.on('data', (chunk) => {
      console.log(`响应内容: ${chunk}`);
    });

    res.on('end', () => {
      if (res.statusCode === 200 || res.statusCode === 202) {
        console.log('✅ IndexNow 提交成功！');
        console.log(`已提交 ${urlList.length} 个URL到搜索引擎`);
        console.log('状态码 202 = 已接受，搜索引擎将在后台处理');
      } else {
        console.log('⚠️ IndexNow 提交失败');
      }
    });
  });

  req.on('error', (e) => {
    console.error(`请求出错: ${e.message}`);
  });

  req.write(postData);
  req.end();
}

// 执行提交
console.log('开始提交URL到IndexNow...');
console.log(`总共 ${urls.length} 个URL`);
submitToIndexNow(urls);
