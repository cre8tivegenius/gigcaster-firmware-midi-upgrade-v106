#!/usr/bin/env python3
"""
Display what's included in the firmware update
"""
import zipfile
from pathlib import Path

zip_file = Path('/Users/aiecan/Downloads/gcs8_sys_v105.zip')

print("=" * 70)
print("GIGCASTER 8 FIRMWARE v105 - WHAT'S INCLUDED")
print("=" * 70)
print()

if not zip_file.exists():
    print(f"ERROR: ZIP file not found")
    exit(1)

with zipfile.ZipFile(zip_file, 'r') as z:
    files = z.namelist()
    
    print(f"Total files in update: {len(files)}")
    print()
    
    # Categorize
    firmware = []
    docs = []
    others = []
    
    for f in files:
        name_lower = f.lower()
        if any(x in name_lower for x in ['.bin', '.sys', '.hex', '.fw', '.rom', '.img']):
            firmware.append(f)
        elif any(x in name_lower for x in ['.txt', '.md', '.pdf', '.html', 'readme', 'release', 'notes', 'changelog']):
            docs.append(f)
        else:
            others.append(f)
    
    print("=" * 70)
    print("FIRMWARE FILES (to copy to device)")
    print("=" * 70)
    if firmware:
        for f in sorted(firmware):
            info = z.getinfo(f)
            size_mb = info.file_size / 1024 / 1024
            print(f"  ✓ {f}")
            print(f"    Size: {size_mb:.2f} MB")
            print()
    else:
        print("  (Checking all files...)")
        for f in files[:10]:
            info = z.getinfo(f)
            if info.file_size > 1024*1024:  # Files > 1MB are likely firmware
                size_mb = info.file_size / 1024 / 1024
                print(f"  ✓ {f} ({size_mb:.2f} MB)")
        print()
    
    print("=" * 70)
    print("DOCUMENTATION / RELEASE NOTES")
    print("=" * 70)
    if docs:
        for f in sorted(docs):
            info = z.getinfo(f)
            size_kb = info.file_size / 1024
            print(f"\n📄 {f} ({size_kb:.1f} KB)")
            print("-" * 70)
            try:
                content = z.read(f).decode('utf-8', errors='ignore')
                print(content)
                print("-" * 70)
            except:
                print("  (Binary file or could not read)")
    else:
        print("\n  No documentation files found in ZIP.")
        print("  Release notes may be:")
        print("    - On Roland's website")
        print("    - In a subdirectory")
        print("    - Embedded in firmware file")
        print()
    
    print("=" * 70)
    print("ALL FILES IN UPDATE")
    print("=" * 70)
    for f in sorted(files)[:50]:
        info = z.getinfo(f)
        if info.file_size > 0:
            if info.file_size < 1024:
                print(f"  {f} ({info.file_size} bytes)")
            elif info.file_size < 1024*1024:
                print(f"  {f} ({info.file_size/1024:.1f} KB)")
            else:
                print(f"  {f} ({info.file_size/1024/1024:.2f} MB)")
        else:
            print(f"  {f}/ (directory)")
    
    if len(files) > 50:
        print(f"  ... and {len(files) - 50} more files")
    
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  • Total files: {len(files)}")
    print(f"  • Firmware files: {len(firmware)}")
    print(f"  • Documentation: {len(docs)}")
    print(f"  • Other files: {len(others)}")
    print()

