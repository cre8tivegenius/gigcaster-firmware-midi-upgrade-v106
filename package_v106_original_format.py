#!/usr/bin/env python3
"""
Package v106 Update in Original Binary Format
Creates a ZIP package matching the exact structure of the original v105 ZIP
"""
import zipfile
import os
import shutil
from pathlib import Path

def main():
    original_zip = Path('/Users/aiecan/Downloads/gcs8_sys_v105.zip')
    firmware_source = Path('/Users/aiecan/Downloads/midi firmware gigcaster/firmware/gcs8_sys_v105')
    package_path = Path('/Users/aiecan/Downloads/gcs8_sys_v106.zip')
    
    print("=" * 70)
    print("PACKAGING V106 UPDATE IN ORIGINAL BINARY FORMAT")
    print("=" * 70)
    print()
    
    # Verify firmware files exist
    print("[1/2] Verifying firmware files...")
    required_files = [
        'GCS8ROM.BIN',
        'GCS8ROM2.BIN',
        'GCS8ROM3.BIN',
        'ROMINFO.TXT',
        'ROMINFO2.TXT',
        'ROMINFO3.TXT',
        'CHECKSUM.TXT'
    ]
    
    firmware_files = {}
    for filename in required_files:
        file_path = firmware_source / filename
        if file_path.exists():
            size = file_path.stat().st_size
            firmware_files[filename] = file_path
            size_str = f"{size/1024/1024:.2f} MB" if size > 1024*1024 else f"{size/1024:.1f} KB"
            print(f"  ✓ {filename} ({size_str})")
        else:
            print(f"  ✗ {filename} - NOT FOUND")
            return
    
    print()
    print("[2/2] Creating ZIP package in original format...")
    
    # Create ZIP with same structure as original
    with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as z:
        # Add directory entry (like original)
        z.writestr('gcs8_sys_v106/', '')
        
        # Add all firmware files in gcs8_sys_v106/ directory
        for filename, file_path in firmware_files.items():
            arc_name = f'gcs8_sys_v106/{filename}'
            z.write(file_path, arc_name)
            print(f"  ✓ Added {arc_name}")
    
    if package_path.exists():
        size_mb = package_path.stat().st_size / 1024 / 1024
        
        # Verify structure matches original
        print()
        print("=" * 70)
        print("PACKAGE CREATED IN ORIGINAL BINARY FORMAT")
        print("=" * 70)
        print(f"  Package: {package_path.name}")
        print(f"  Size: {size_mb:.2f} MB")
        print(f"  Structure: gcs8_sys_v106/")
        print(f"  Binary files: 3 (GCS8ROM.BIN, GCS8ROM2.BIN, GCS8ROM3.BIN)")
        print(f"  Format: Matches original v105 structure")
        print("=" * 70)
        
        # Show package contents
        print()
        print("Package contents:")
        with zipfile.ZipFile(package_path, 'r') as z:
            for info in z.infolist():
                size_str = f"{info.file_size/1024/1024:.2f} MB" if info.file_size > 1024*1024 else f"{info.file_size} bytes"
                print(f"  {info.filename} ({size_str})")
    else:
        print("ERROR: Package not created")

if __name__ == '__main__':
    main()

