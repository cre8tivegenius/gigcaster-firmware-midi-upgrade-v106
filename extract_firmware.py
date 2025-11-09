#!/usr/bin/env python3
"""
Gigcaster 8 Firmware Extraction Script
Extracts gcs8_sys_v105.zip to the firmware directory
"""
import zipfile
import os
import sys
import shutil
from pathlib import Path

zip_path = Path('/Users/aiecan/Downloads/gcs8_sys_v105.zip')
extract_to = Path('/Users/aiecan/Downloads/midi firmware gigcaster/firmware')

def main():
    print("=" * 60)
    print("Gigcaster 8 Firmware Extraction")
    print("=" * 60)
    print(f"\nZIP file: {zip_path}")
    print(f"Exists: {zip_path.exists()}")
    
    if not zip_path.exists():
        print(f"\nERROR: ZIP file not found at {zip_path}")
        sys.exit(1)
    
    # Create destination directory
    extract_to.mkdir(parents=True, exist_ok=True)
    
    # Backup README if it exists
    readme_backup = None
    readme_path = extract_to / 'README.md'
    if readme_path.exists():
        readme_backup = extract_to / 'README.md.bak'
        shutil.move(str(readme_path), str(readme_backup))
        print(f"\nBacked up existing README.md")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            files = zip_ref.namelist()
            print(f"\nFound {len(files)} files in ZIP archive")
            print("\nFirst 20 files:")
            for i, name in enumerate(files[:20], 1):
                info = zip_ref.getinfo(name)
                size_kb = info.file_size / 1024
                print(f"  {i:2d}. {name} ({size_kb:.1f} KB)")
            
            if len(files) > 20:
                print(f"  ... and {len(files) - 20} more files")
            
            print(f"\nExtracting to: {extract_to}")
            zip_ref.extractall(extract_to)
            print("✓ Extraction complete!")
            
            # Restore README
            if readme_backup and readme_backup.exists():
                shutil.move(str(readme_backup), str(readme_path))
                print("✓ Restored README.md")
            
            # List extracted files
            print(f"\nExtracted files in {extract_to}:")
            extracted_files = []
            for root, dirs, files in os.walk(extract_to):
                # Skip hidden files and README
                files = [f for f in files if not f.startswith('.') and f != 'README.md']
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                
                level = Path(root).relative_to(extract_to).parts
                indent = '  ' * len(level)
                
                if level:
                    print(f"{indent}{Path(root).name}/")
                
                for file in sorted(files)[:15]:
                    file_path = Path(root) / file
                    size = file_path.stat().st_size
                    size_str = f"({size/1024:.1f} KB)" if size > 0 else ""
                    print(f"{indent}  {file} {size_str}")
                    extracted_files.append(file_path.relative_to(extract_to))
            
            if len(extracted_files) > 15:
                print(f"  ... and {len(extracted_files) - 15} more files")
            
            print(f"\n✓ Successfully extracted {len(extracted_files)} files")
            print("\nNext steps:")
            print("1. Verify all firmware files are in the firmware/ directory")
            print("2. Ensure files are at root level (not in subfolders)")
            print("3. Follow update instructions in README.md")
            
    except zipfile.BadZipFile:
        print(f"\nERROR: {zip_path} is not a valid ZIP file")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()

