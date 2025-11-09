#!/usr/bin/env python3
"""
Binary Firmware Extractor and Package Creator
Extracts binary firmware files and creates v106 package with binaries
"""
import zipfile
import os
import shutil
from pathlib import Path

def main():
    import sys
    
    original_zip = Path('/Users/aiecan/Downloads/gcs8_sys_v105.zip')
    firmware_dest = Path('/Users/aiecan/Downloads/midi firmware gigcaster/firmware')
    package_path = Path('/Users/aiecan/Downloads/gigcaster8_firmware_v106_update_package.zip')
    project_root = Path('/Users/aiecan/Downloads/midi firmware gigcaster')
    
    print("=" * 70, file=sys.stderr)
    print("EXTRACTING BINARY FIRMWARE & CREATING V106 PACKAGE", file=sys.stderr)
    print("=" * 70, file=sys.stderr)
    print(file=sys.stderr)
    
    # Extract binary firmware files
    print("[1/3] Extracting binary firmware files...", file=sys.stderr)
    if not original_zip.exists():
        print(f"ERROR: Original ZIP not found at {original_zip}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found ZIP: {original_zip}", file=sys.stderr)
    
    # Backup README
    readme_bak = None
    if (firmware_dest / 'README.md').exists():
        readme_bak = firmware_dest / 'README.md.bak'
        shutil.move(str(firmware_dest / 'README.md'), str(readme_bak))
    
    try:
        with zipfile.ZipFile(original_zip, 'r') as z:
            files = z.namelist()
            print(f"     Found {len(files)} files in original ZIP", file=sys.stderr)
            
            # Identify binary files BEFORE extraction
            binary_files = []
            for f in files:
                info = z.getinfo(f)
                if info.file_size > 1000:
                    name_lower = f.lower()
                    if (any(ext in name_lower for ext in ['.bin', '.sys', '.hex', '.fw', '.rom', '.img', '.dat']) or 
                        info.file_size > 100000):
                        binary_files.append((f, info.file_size))
            
            firmware_dest.mkdir(parents=True, exist_ok=True)
            z.extractall(firmware_dest)
            print(f"     ✓ Extracted all files (including binary firmware)", file=sys.stderr)
        
        if binary_files:
            print(f"\n     Binary firmware files:", file=sys.stderr)
            for f, size in binary_files[:10]:
                size_mb = size / 1024 / 1024
                print(f"       ✓ {f} ({size_mb:.2f} MB)", file=sys.stderr)
    except Exception as e:
        print(f"ERROR extracting ZIP: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    
    # Restore README
    if readme_bak and readme_bak.exists():
        shutil.move(str(readme_bak), str(firmware_dest / 'README.md'))
    
    print(file=sys.stderr)
    
    # Create package with binaries
    print("[2/3] Creating ZIP package with binary firmware files...", file=sys.stderr)
    files_to_include = []
    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        root_path = Path(root)
        for file in files:
            if not file.endswith(('.bak', '.pyc', '.DS_Store')):
                file_path = root_path / file
                rel_path = file_path.relative_to(project_root.parent)
                files_to_include.append((file_path, rel_path))
    
    binary_count = sum(1 for f, _ in files_to_include if f.exists() and f.stat().st_size > 10000)
    print(f"     Found {len(files_to_include)} files", file=sys.stderr)
    print(f"     Binary files (>10KB): {binary_count}", file=sys.stderr)
    
    print(file=sys.stderr)
    print("[3/3] Packaging files...", file=sys.stderr)
    try:
        with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as z:
            for file_path, arc_name in sorted(files_to_include):
                if file_path.exists():
                    z.write(file_path, arc_name)
    except Exception as e:
        print(f"ERROR creating package: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    
    if package_path.exists():
        size_mb = package_path.stat().st_size / 1024 / 1024
        print(file=sys.stderr)
        print("=" * 70, file=sys.stderr)
        print("PACKAGE CREATED WITH BINARY FIRMWARE FILES", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
        print(f"  Package: {package_path.name}", file=sys.stderr)
        print(f"  Size: {size_mb:.2f} MB", file=sys.stderr)
        print(f"  Total files: {len(files_to_include)}", file=sys.stderr)
        print(f"  Binary files: {binary_count}", file=sys.stderr)
        print(f"  Version: gcs8_sys_v106", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
    else:
        print("ERROR: Package not created", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

