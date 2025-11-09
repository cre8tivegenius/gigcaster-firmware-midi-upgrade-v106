#!/usr/bin/env python3
"""
Verify firmware extraction
"""
from pathlib import Path

firmware_dir = Path('/Users/aiecan/Downloads/midi firmware gigcaster/firmware')

print("Checking firmware directory...")
print(f"Path: {firmware_dir}")
print(f"Exists: {firmware_dir.exists()}")

if firmware_dir.exists():
    all_items = list(firmware_dir.iterdir())
    files = [f for f in all_items if f.is_file() and f.name != 'README.md']
    dirs = [d for d in all_items if d.is_dir()]
    
    print(f"\nTotal items: {len(all_items)}")
    print(f"Files (excluding README.md): {len(files)}")
    print(f"Directories: {len(dirs)}")
    
    if files:
        print("\nFiles found:")
        for f in sorted(files):
            size = f.stat().st_size
            print(f"  {f.name} ({size:,} bytes)")
    
    if dirs:
        print("\nDirectories found:")
        for d in sorted(dirs):
            print(f"  {d.name}/")
            # List contents of subdirectories
            subitems = list(d.iterdir())
            for item in sorted(subitems)[:10]:
                if item.is_file():
                    size = item.stat().st_size
                    print(f"    {item.name} ({size:,} bytes)")
                else:
                    print(f"    {item.name}/")
    
    if not files and not dirs:
        print("\n⚠️  No firmware files found!")
        print("   Run: python3 extract_firmware.py")
    else:
        print(f"\n✓ Found {len(files)} files and {len(dirs)} directories")

