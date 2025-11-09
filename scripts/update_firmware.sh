#!/bin/bash
# Gigcaster 8 Firmware Update Script
# Version: gcs8_sys_v105

set -e

FIRMWARE_DIR="firmware"
DEVICE_NAME="GCS-8_INT"

echo "=== Gigcaster 8 Firmware Update Script ==="
echo "Target Version: gcs8_sys_v105"
echo ""

# Check if firmware directory exists
if [ ! -d "$FIRMWARE_DIR" ]; then
    echo "Error: Firmware directory not found!"
    exit 1
fi

# Check if device is mounted
if [ ! -d "/Volumes/$DEVICE_NAME" ]; then
    echo "Error: Gigcaster 8 not found!"
    echo "Please:"
    echo "1. Turn off Gigcaster 8"
    echo "2. Press and hold [MARK] button while turning on"
    echo "3. Connect via USB"
    echo "4. Wait for 'CONNECTED' message"
    exit 1
fi

echo "Gigcaster 8 found at /Volumes/$DEVICE_NAME"
echo ""
echo "Ready to copy firmware files..."
echo "Press Enter to continue or Ctrl+C to cancel"
read

# Copy firmware files
echo "Copying firmware files..."
cp -v "$FIRMWARE_DIR"/* "/Volumes/$DEVICE_NAME/" 2>/dev/null || {
    echo "Error copying files. Make sure firmware files are in $FIRMWARE_DIR/"
    exit 1
}

echo ""
echo "Files copied successfully!"
echo ""
echo "Next steps:"
echo "1. Safely eject /Volumes/$DEVICE_NAME"
echo "2. On Gigcaster 8, press [REC] when 'UPDATE ?' appears"
echo "3. Wait for 'COMPLETE' message"
echo "4. Power off and back on"

