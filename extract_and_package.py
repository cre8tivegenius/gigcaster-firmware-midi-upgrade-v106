#!/usr/bin/env python3
"""
Extract binary firmware and create v106 package
Writes output to result.txt for debugging
"""
import zipfile
import os
import shutil
from pathlib import Path
import sys

def main():
    original_zip = Path('/Users/aiecan/Downloads/gcs8_sys_v105.zip')
    firmware_dest = Path('/Users/aiecan/Downloads/midi firmware gigcaster/firmware')
    package_path = Path('/Users/aiecan/Downloads/gigcaster8_firmware_v106_update_package.zip')
    project_root = Path('/Users/aiecan/Downloads/midi firmware gigcaster')
    result_file = Path('/tmp/extract_result.txt')
    
    with open(result_file, 'w') as out:
        out.write("=" * 70 + "\n")
        out.write("EXTRACTING BINARY FIRMWARE & CREATING V106 PACKAGE\n")
        out.write("=" * 70 + "\n\n")
        
        # Check ZIP exists
        if not original_zip.exists():
            out.write(f"ERROR: ZIP not found at {original_zip}\n")
            return
        
        out.write(f"[1/3] Extracting from: {original_zip}\n")
        
        # Backup README
        readme_bak = None
        if (firmware_dest / 'README.md').exists():
            readme_bak = firmware_dest / 'README.md.bak'
            shutil.move(str(firmware_dest / 'README.md'), str(readme_bak))
        
        try:
            with zipfile.ZipFile(original_zip, 'r') as z:
                files = z.namelist()
                out.write(f"     Found {len(files)} files in ZIP\n")
                
                # Identify binary files
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
                out.write(f"     ✓ Extracted all files\n")
                
                if binary_files:
                    out.write(f"\n     Binary firmware files found:\n")
                    for f, size in binary_files[:10]:
                        size_mb = size / 1024 / 1024
                        out.write(f"       ✓ {f} ({size_mb:.2f} MB)\n")
        
        except Exception as e:
            out.write(f"ERROR: {e}\n")
            import traceback
            traceback.print_exc(file=out)
            return
        
        # Restore README
        if readme_bak and readme_bak.exists():
            shutil.move(str(readme_bak), str(firmware_dest / 'README.md'))
        
        # Create package
        out.write(f"\n[2/3] Creating package...\n")
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
        out.write(f"     Found {len(files_to_include)} files\n")
        out.write(f"     Binary files (>10KB): {binary_count}\n")
        
        out.write(f"\n[3/3] Packaging...\n")
        try:
            with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as z:
                for file_path, arc_name in sorted(files_to_include):
                    if file_path.exists():
                        z.write(file_path, arc_name)
        except Exception as e:
            out.write(f"ERROR creating package: {e}\n")
            import traceback
            traceback.print_exc(file=out)
            return
        
        if package_path.exists():
            size_mb = package_path.stat().st_size / 1024 / 1024
            out.write("\n" + "=" * 70 + "\n")
            out.write("PACKAGE CREATED WITH BINARY FIRMWARE FILES\n")
            out.write("=" * 70 + "\n")
            out.write(f"  Package: {package_path.name}\n")
            out.write(f"  Size: {size_mb:.2f} MB\n")
            out.write(f"  Total files: {len(files_to_include)}\n")
            out.write(f"  Binary files: {binary_count}\n")
            out.write(f"  Version: gcs8_sys_v106\n")
            out.write("=" * 70 + "\n")
        else:
            out.write("ERROR: Package not created\n")
    
    # Print result
    if result_file.exists():
        with open(result_file, 'r') as f:
            print(f.read())

if __name__ == '__main__':
    main()

