# LIHUA Electronics

台山市利华电子厂有限公司的中英双语静态官网。项目不依赖前端框架或运行时服务，适合部署到 GitHub Pages、Cloudflare Pages 或其他静态托管平台。

## 页面

- `/`：按浏览器语言跳转到 `/zh/` 或 `/en/`
- `/zh/`、`/en/`：首页
- `/zh/manufacturing.html`、`/en/manufacturing.html`：制造能力
- `/zh/about.html`、`/en/about.html`：关于利华
- `/zh/contact.html`、`/en/contact.html`：联系方式

## 本地预览

```bash
python3 -m http.server 8765
```

然后打开 <http://127.0.0.1:8765/>。

## 更新页面

页面文案和结构的主要来源是 `build-pages.py` 中的 `I18N` 数据。修改后重新生成双语页面：

```bash
python3 build-pages.py
```

全站样式在 `css/site.css`，语言跳转逻辑在 `js/site.js`，图片在 `assets/`。

## 项目边界

公开仓库只包含可发布的站点文件和页面生成脚本。PPT 解压原料、生产环境操作说明、备份素材和本机环境文件被 `.gitignore` 排除，不应提交到公开仓库。
