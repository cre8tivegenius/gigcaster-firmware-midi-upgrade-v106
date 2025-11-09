#!/usr/bin/env python3
"""
Tool Checker - Verify all required tools are available
"""
import sys
import subprocess
import importlib

def check_tool(name, check_command=None, import_name=None):
    """Check if a tool/module is available"""
    if import_name:
        try:
            importlib.import_module(import_name)
            return True, f"✓ {name} (Python module)"
        except ImportError:
            return False, f"✗ {name} (Python module) - MISSING"
    
    if check_command:
        try:
            result = subprocess.run(check_command, shell=True, 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                output = result.stdout.strip().split('\n')[0]
                return True, f"✓ {name}: {output}"
            else:
                return False, f"✗ {name} - NOT FOUND"
        except Exception as e:
            return False, f"✗ {name} - ERROR: {e}"
    
    return None, ""

print("=" * 60)
print("REQUIRED TOOLS CHECK")
print("=" * 60)
print()

# Check Python
python_version = sys.version.split()[0]
print(f"✓ Python {python_version} installed")
print(f"  Path: {sys.executable}")
print()

# Check Python standard library modules
print("Python Standard Library Modules:")
print("-" * 60)
required_modules = [
    ('zipfile', 'ZIP file handling'),
    ('json', 'JSON processing'),
    ('shutil', 'File operations'),
    ('pathlib', 'Path handling'),
    ('os', 'OS interface'),
    ('datetime', 'Date/time handling'),
]

all_modules_ok = True
for mod_name, description in required_modules:
    try:
        importlib.import_module(mod_name)
        print(f"  ✓ {mod_name:12} - {description}")
    except ImportError:
        print(f"  ✗ {mod_name:12} - {description} - MISSING!")
        all_modules_ok = False

print()

# Check system commands
print("System Commands:")
print("-" * 60)
commands = [
    ('unzip', 'which unzip && unzip -v 2>&1 | head -1'),
    ('chmod', 'which chmod'),
    ('ls', 'which ls'),
]

all_commands_ok = True
for cmd_name, check_cmd in commands:
    ok, msg = check_tool(cmd_name, check_cmd)
    if ok:
        print(f"  {msg}")
    else:
        print(f"  {msg}")
        all_commands_ok = False

print()
print("=" * 60)
if all_modules_ok and all_commands_ok:
    print("✓ ALL TOOLS AVAILABLE - Ready to proceed!")
    print("=" * 60)
    sys.exit(0)
else:
    print("✗ SOME TOOLS MISSING - Please install missing tools")
    print("=" * 60)
    sys.exit(1)

