from pathlib import Path

directory_path = Path("/Users/alora/Maktab/sending projects/hw7/untitled folder/MaktabsharifMiniProject3/front/images")

file_pattern = "*-icon.png"
second_file_pattern = "*-icon-1.png"

matching_files = directory_path.glob(file_pattern)
matched_files = ""
for file_path in matching_files:
    matched_files += f"{str(file_path)}\n"

matching_files = directory_path.glob(second_file_pattern)
for file_path in matching_files:
    matched_files += f"{str(file_path)}\n"
    
Path('Icons.txt').write_text(str(matched_files))
