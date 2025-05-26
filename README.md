# StaticFusion

**StaticFusion** is a lightweight Python tool created by **Enock** to build production-ready static HTML websites from modular components like headers and footers.


## 🔧 Features

- ✅ Parses `components.js` to detect dynamic imports like:
  ```js
  fetch('components/header.html')
  ```
- ✅ Replaces `<div id="header"></div>` with the actual HTML content from `components/header.html`
- ✅ Removes the need for JavaScript `fetch()` calls in the final output
- ✅ Recursively processes all `.html` files in the project directory
- ✅ Copies all supporting assets (CSS, JS, images, etc.)
- ✅ Outputs clean, zipped static HTML files in a `dist/` folder

---

## 📁 Folder Structure Example

```
your-project/
├── components/
│   ├── header.html
│   └── footer.html
├── components.js
├── index.html
├── about.html
├── contact.html
└── build_pages.py
```

---

## 🚀 How to Use

1. **Prepare your modular project** using `fetch()` to include components in `components.js`.
2. **Run the script**:
   ```bash
   python3 build_pages.py
   ```
3. The script will:
   - Inject component HTML into your HTML files
   - Copy all assets (CSS, JS, images, etc.)
   - Save everything in the `dist/` folder
   - Create a ZIP: `html_component_combined_with_assets.zip`


## 📦 Output

- ✅ `dist/` folder with:
  - Injected static HTML files
  - All necessary assets
- ✅ `html_component_combined_with_assets.zip` for deployment or sharing


## 👨‍💻 Author

**Enock**

> Simplifying the web, one static build at a time.# StaticFusion
