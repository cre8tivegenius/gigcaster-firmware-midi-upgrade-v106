#!/usr/bin/env python3
"""
Extract firmware and create detailed report
"""
import zipfile
import json
from pathlib import Path
from datetime import datetime

zip_file = Path('/Users/aiecan/Downloads/gcs8_sys_v105.zip')
dest = Path('/Users/aiecan/Downloads/midi firmware gigcaster/firmware')
report_file = dest / 'EXTRACTION_REPORT.txt'

# Extract ZIP
print("Extracting firmware...")
with zipfile.ZipFile(zip_file, 'r') as z:
    files = z.namelist()
    z.extractall(dest)
    print(f"Extracted {len(files)} files")

# Analyze and create report
with open(report_file, 'w') as f:
    f.write("=" * 70 + "\n")
    f.write("GIGCASTER 8 FIRMWARE v105 EXTRACTION REPORT\n")
    f.write("=" * 70 + "\n\n")
    f.write(f"Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"ZIP File: {zip_file}\n")
    f.write(f"Destination: {dest}\n\n")
    
    # Categorize files
    firmware_files = []
    doc_files = []
    other_files = []
    
    for file_path in files:
        name_lower = file_path.lower()
        if any(ext in name_lower for ext in ['.bin', '.sys', '.hex', '.fw', '.rom']):
            firmware_files.append(file_path)
        elif any(ext in name_lower for ext in ['.txt', '.md', '.pdf', '.html', 'readme', 'release', 'notes']):
            doc_files.append(file_path)
        else:
            other_files.append(file_path)
    
    f.write(f"FILE BREAKDOWN:\n")
    f.write(f"  • Total files: {len(files)}\n")
    f.write(f"  • Firmware files: {len(firmware_files)}\n")
    f.write(f"  • Documentation: {len(doc_files)}\n")
    f.write(f"  • Other files: {len(other_files)}\n\n")
    
    # List firmware files
    if firmware_files:
        f.write("FIRMWARE FILES:\n")
        f.write("-" * 70 + "\n")
        with zipfile.ZipFile(zip_file, 'r') as z:
            for file_path in sorted(firmware_files):
                info = z.getinfo(file_path)
                size_mb = info.file_size / 1024 / 1024
                f.write(f"  ✓ {file_path}\n")
                f.write(f"    Size: {size_mb:.2f} MB\n\n")
    
    # Read and include documentation
    if doc_files:
        f.write("\nDOCUMENTATION FILES:\n")
        f.write("-" * 70 + "\n")
        with zipfile.ZipFile(zip_file, 'r') as z:
            for file_path in sorted(doc_files):
                info = z.getinfo(file_path)
                size_kb = info.file_size / 1024
                f.write(f"\n📄 {file_path} ({size_kb:.1f} KB)\n")
                f.write("-" * 70 + "\n")
                try:
                    content = z.read(file_path).decode('utf-8', errors='ignore')
                    f.write(content)
                    f.write("\n")
                except Exception as e:
                    f.write(f"Could not read: {e}\n")
                f.write("-" * 70 + "\n")
    
    # List other files
    if other_files:
        f.write(f"\nOTHER FILES ({len(other_files)}):\n")
        f.write("-" * 70 + "\n")
        for file_path in sorted(other_files)[:30]:
            f.write(f"  • {file_path}\n")
        if len(other_files) > 30:
            f.write(f"  ... and {len(other_files) - 30} more\n")

print(f"Report saved to: {report_file}")

