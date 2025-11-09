#!/usr/bin/env python3
"""
Export Package v106 - Create ZIP package of firmware update project
"""
import zipfile
import os
from pathlib import Path
from datetime import datetime

def create_package():
    """Create ZIP package of the firmware update project for v106"""
    
    project_root = Path('/Users/aiecan/Downloads/midi firmware gigcaster')
    package_name = 'gigcaster8_firmware_v106_update_package.zip'
    package_path = Path('/Users/aiecan/Downloads') / package_name
    
    print("=" * 70)
    print("CREATING FIRMWARE UPDATE PACKAGE v106")
    print("=" * 70)
    print()
    print(f"Project: {project_root}")
    print(f"Package: {package_path}")
    print()
    
    # Collect files
    files_to_include = []
    
    for root, dirs, files in os.walk(project_root):
        # Skip hidden and cache directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        root_path = Path(root)
        
        for file in files:
            # Skip backup and cache files
            if file.endswith(('.bak', '.pyc', '.DS_Store')):
                continue
            
            file_path = root_path / file
            # Get relative path from Downloads directory
            rel_path = file_path.relative_to(project_root.parent)
            files_to_include.append((file_path, rel_path))
    
    print(f"Found {len(files_to_include)} files to package")
    print()
    
    # Create ZIP package
    print("Creating ZIP package...")
    with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for file_path, arc_name in sorted(files_to_include):
            if file_path.exists():
                z.write(file_path, arc_name)
                print(f"  ✓ {arc_name}")
    
    # Get package info
    size_mb = package_path.stat().st_size / 1024 / 1024
    
    print()
    print("=" * 70)
    print("PACKAGE CREATED SUCCESSFULLY")
    print("=" * 70)
    print(f"  Package: {package_path.name}")
    print(f"  Location: {package_path.parent}")
    print(f"  Size: {size_mb:.2f} MB")
    print(f"  Files: {len(files_to_include)}")
    print(f"  Version: gcs8_sys_v106")
    print()
    print("Package is ready to:")
    print("  • Share with others")
    print("  • Archive for future reference")
    print("  • Use on other systems")
    print("=" * 70)

if __name__ == '__main__':
    create_package()

