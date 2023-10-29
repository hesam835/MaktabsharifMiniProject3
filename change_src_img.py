from pathlib import Path
import re

directory_path = Path(r"C:\Users\Mahdi\Desktop\MaktabsharifMiniProject3\front")
html_pattern = "*.html"

html_file_path = directory_path.glob(html_pattern)
html_files = [x for x in html_file_path]
img_pattern = r'<img src="(images)\/.*(-icon|-icon-1)\.png">'
for html_file in html_files:
    print(html_file)
    with open(html_file, "r") as f:
        content = f.read()
        result = re.finditer(img_pattern, content, flags= re.M)
        print(type(result))
        for img in result:
            print(img.group())

