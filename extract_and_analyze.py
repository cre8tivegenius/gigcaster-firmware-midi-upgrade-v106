#!/usr/bin/env python3
"""
Extract and analyze Gigcaster 8 firmware v105
"""
import zipfile
import os
import shutil
from pathlib import Path
import json
from datetime import datetime

zip_file = Path('/Users/aiecan/Downloads/gcs8_sys_v105.zip')
dest = Path('/Users/aiecan/Downloads/midi firmware gigcaster/firmware')
report_file = dest / 'gcs8_sys_v105_aggressive_report_v2.json'

print("=" * 70)
print("GIGCASTER 8 FIRMWARE v105 EXTRACTION & ANALYSIS")
print("=" * 70)

# Check ZIP exists
if not zip_file.exists():
    print(f"\nERROR: ZIP file not found at {zip_file}")
    exit(1)

print(f"\nZIP file: {zip_file}")
print(f"Size: {zip_file.stat().st_size / 1024 / 1024:.2f} MB")

# Backup existing files
readme_bak = None
report_bak = None
if (dest / 'README.md').exists():
    readme_bak = dest / 'README.md.bak'
    shutil.move(str(dest / 'README.md'), str(readme_bak))
if report_file.exists():
    report_bak = dest / 'gcs8_sys_v105_aggressive_report_v2.json.bak'
    shutil.move(str(report_file), str(report_bak))

# Extract ZIP
print(f"\nExtracting to: {dest}")
dest.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(zip_file, 'r') as z:
    files = z.namelist()
    print(f"Files in ZIP: {len(files)}")
    
    z.extractall(dest)
    print("✓ Extraction complete")

# Restore backups
if readme_bak and readme_bak.exists():
    shutil.move(str(readme_bak), str(dest / 'README.md'))
if report_bak and report_bak.exists():
    shutil.move(str(report_bak), str(report_file))

# Analyze extracted files
print(f"\nAnalyzing extracted files...")
all_items = [f for f in dest.iterdir() 
             if f.name not in ['README.md', 'gcs8_sys_v105_aggressive_report_v2.json',
                               'README.md.bak', 'gcs8_sys_v105_aggressive_report_v2.json.bak']]

firmware_files = []
doc_files = []
other_files = []

for item in all_items:
    name_lower = item.name.lower()
    if any(ext in name_lower for ext in ['.bin', '.sys', '.hex', '.fw', '.rom', '.img']):
        firmware_files.append(item)
    elif any(ext in name_lower for ext in ['.txt', '.md', '.pdf', '.html', '.rtf']):
        doc_files.append(item)
    elif item.is_dir():
        # Check subdirectory
        for sub in item.iterdir():
            if sub.is_file():
                sub_name_lower = sub.name.lower()
                if any(ext in sub_name_lower for ext in ['.bin', '.sys', '.hex', '.fw', '.rom']):
                    firmware_files.append(sub)
                elif any(ext in sub_name_lower for ext in ['.txt', '.md', '.pdf', '.html']):
                    doc_files.append(sub)
        other_files.append(item)
    else:
        other_files.append(item)

print(f"\nFile breakdown:")
print(f"  • Firmware files: {len(firmware_files)}")
print(f"  • Documentation: {len(doc_files)}")
print(f"  • Other files/dirs: {len(other_files)}")

# Show firmware files
if firmware_files:
    print(f"\n🔧 FIRMWARE FILES:")
    for f in sorted(firmware_files):
        size_mb = f.stat().st_size / 1024 / 1024
        print(f"   ✓ {f.name} ({size_mb:.2f} MB)")

# Show and read documentation
if doc_files:
    print(f"\n📄 DOCUMENTATION FILES:")
    for f in sorted(doc_files):
        size_kb = f.stat().st_size / 1024
        print(f"   {f.name} ({size_kb:.1f} KB)")
        
        # Read text files
        if f.suffix.lower() in ['.txt', '.md', '.html']:
            try:
                content = f.read_text(encoding='utf-8', errors='ignore')
                if len(content.strip()) > 0:
                    print(f"   ──────────────────────────────────────────────────────────")
                    print(f"   {content[:1000]}")
                    if len(content) > 1000:
                        print(f"   ... (truncated, {len(content)} total characters)")
                    print(f"   ──────────────────────────────────────────────────────────")
            except Exception as e:
                print(f"   (Could not read: {e})")

# Show other files
if other_files:
    print(f"\n📁 OTHER FILES/DIRECTORIES:")
    for f in sorted(other_files)[:20]:
        if f.is_file():
            size_kb = f.stat().st_size / 1024
            print(f"   • {f.name} ({size_kb:.1f} KB)")
        else:
            print(f"   📁 {f.name}/")
            for sub in sorted(f.iterdir())[:5]:
                if sub.is_file():
                    print(f"      {sub.name}")

print("\n" + "=" * 70)
print("EXTRACTION COMPLETE")
print("=" * 70)

