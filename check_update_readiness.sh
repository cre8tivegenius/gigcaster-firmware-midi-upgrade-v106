#!/bin/bash
# Quick Update Checklist Script
# Run this before starting the firmware update

echo "=========================================="
echo "Gigcaster 8 Firmware Update Checklist"
echo "=========================================="
echo ""

FIRMWARE_DIR="/Users/aiecan/Downloads/midi firmware gigcaster/firmware"

echo "1. Checking firmware files..."
if [ -d "$FIRMWARE_DIR" ]; then
    FILE_COUNT=$(find "$FIRMWARE_DIR" -type f ! -name "README.md" ! -name "*.json" | wc -l | tr -d ' ')
    echo "   ✓ Firmware directory exists"
    echo "   ✓ Found $FILE_COUNT firmware files"
    
    if [ "$FILE_COUNT" -eq 0 ]; then
        echo "   ⚠ WARNING: No firmware files found!"
        echo "   Run: python3 extract_firmware.py"
    fi
else
    echo "   ✗ Firmware directory not found!"
fi

echo ""
echo "2. Pre-update checklist:"
echo "   [ ] Current firmware version checked"
echo "   [ ] USB data cable ready"
echo "   [ ] Computer USB port available"
echo "   [ ] Stable power supply"
echo "   [ ] All USB apps closed"
echo ""
echo "3. Ready to proceed?"
echo "   Review UPDATE_GUIDE.md for detailed instructions"
echo ""
echo "=========================================="

