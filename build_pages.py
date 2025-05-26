import os
import re
import shutil

# === CONFIG ===
components_js_path = 'components.js'
components_dir = 'components'
output_dir = 'dist'
exclude_dirs = {'dist', '.git', '__pycache__'}
exclude_files = {'build_pages.py'}

# === STEP 1: Extract reusable component fetch paths from components.js ===
with open(components_js_path, 'r') as f:
    js_content = f.read()

component_fetches = re.findall(r"fetch\(['\"](components/[^'\"]+)['\"]\)", js_content)

# === STEP 2: Load each component's HTML content ===
components = {}
for path in component_fetches:
    component_name = os.path.splitext(os.path.basename(path))[0]
    full_path = os.path.join(components_dir, f"{component_name}.html")
    if os.path.exists(full_path):
        with open(full_path, 'r') as f:
            components[component_name] = f.read()

# === STEP 3: Inject components into all HTML files ===
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for root, dirs, files in os.walk('.'):
    # Skip excluded directories
    if any(excluded in root for excluded in exclude_dirs):
        continue

    for file in files:
        if file.endswith('.html') and file not in exclude_files:
            html_path = os.path.join(root, file)
            with open(html_path, 'r') as f:
                html_content = f.read()

            # Inject component content in place of divs with matching IDs
            for name, content in components.items():
                html_content = re.sub(
                    rf'<div\s+id=["\']{name}["\']\s*>\s*</div>',
                    content,
                    html_content,
                    flags=re.IGNORECASE
                )

            # OPTIONAL: Remove <script src="components.js"> line
            html_content = re.sub(
                r'<script\s+src=["\']components\.js["\']\s*>\s*</script>',
                '',
                html_content,
                flags=re.IGNORECASE
            )

            # Save updated file
            rel_path = os.path.relpath(html_path, '.')
            output_path = os.path.join(output_dir, rel_path)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w') as f:
                f.write(html_content)

# === STEP 4: Copy remaining assets (CSS, JS, images, etc.) ===
for root, dirs, files in os.walk('.'):
    if any(excl in root for excl in exclude_dirs):
        continue
    for file in files:
        if file in exclude_files or file.endswith('.html'):
            continue
        src_path = os.path.join(root, file)
        rel_path = os.path.relpath(src_path, '.')
        dest_path = os.path.join(output_dir, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(src_path, dest_path)

# === STEP 5: Create ZIP archive of the output directory ===
shutil.make_archive('static', 'zip', output_dir)
print("✅ Static site built and zipped successfully!")
