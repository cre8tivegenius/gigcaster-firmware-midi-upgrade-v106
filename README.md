# Gigcaster 8 Firmware MIDI Upgrade v106

Boss Gigcaster firmware upgrade to include MIDI functionality through USB.

## Overview

This repository contains the firmware update package for Roland Gigcaster 8 (Boss Gigcaster) version 106, which adds MIDI functionality through USB connectivity.

## ⚠️ Important Notes

- **Use at your own risk**: Firmware updates can potentially damage your device if not performed correctly
- **Backup your settings**: Save any important device configurations before updating
- **Stable power**: Ensure your device has stable power during the update process
- **Do not interrupt**: Never power off or disconnect USB during firmware update

## Package Contents

The firmware package (`gcs8_sys_v106.zip`) includes:

- **GCS8ROM.BIN** (12 MB) - Main firmware binary
- **GCS8ROM2.BIN** (12 MB) - Secondary firmware binary  
- **GCS8ROM3.BIN** (8 MB) - Tertiary firmware binary
- **ROMINFO.TXT** - ROM information
- **ROMINFO2.TXT** - Secondary ROM information
- **ROMINFO3.TXT** - Tertiary ROM information
- **CHECKSUM.TXT** - Checksum verification

## Installation Instructions

1. **Download the firmware package**
   - Download `gcs8_sys_v106.zip` from the [Releases](../../releases) page

2. **Extract the ZIP file**
   - Extract `gcs8_sys_v106.zip` to a location on your computer
   - Ensure all files are extracted to the `gcs8_sys_v106/` folder

3. **Prepare your Gigcaster 8**
   - Connect your Gigcaster 8 to your computer via USB cable (ensure it supports data transfer)
   - Power on your Gigcaster 8
   - The device should appear as a USB drive named `GCS-8_INT`

4. **Transfer firmware files**
   - Copy **ALL files** from the `gcs8_sys_v106/` folder to the **root** of the `GCS-8_INT` drive
   - **Important**: Files must be at the root level, not in a subfolder
   - Ensure all files are copied completely

5. **Start the update**
   - Safely eject the USB drive
   - The Gigcaster 8 should automatically detect the firmware files
   - Follow the on-screen prompts on your Gigcaster 8
   - **DO NOT** power off or disconnect USB during the update

6. **Verify installation**
   - After update completes, power cycle your device
   - Check the firmware version in device settings
   - Test MIDI functionality through USB

## Troubleshooting

### Device Not Detected
- Try a different USB cable (must support data transfer)
- Try a different USB port
- Restart device in update mode (hold MARK button while powering on)
- Check device drivers/managers

### Update Fails
- Ensure all files are at the root of `GCS-8_INT` drive (not in subfolder)
- Re-extract firmware files from ZIP
- Re-download firmware package
- Check available disk space on device

### MIDI Not Working
- Verify firmware version is v106
- Check USB cable connection
- Restart device after firmware update
- Consult device manual for MIDI settings

## Version Information

- **Current Version**: gcs8_sys_v106
- **Previous Version**: gcs8_sys_v105
- **Device**: Roland Gigcaster 8 (Boss Gigcaster)

## Features

- ✅ MIDI functionality through USB
- ✅ Improved USB connectivity
- ✅ Enhanced device stability

## License

This firmware update package is provided under the [CC0-1.0 License](LICENSE) - Creative Commons Zero v1.0 Universal.

## Disclaimer

This firmware is provided "as-is" without any warranties. Use at your own risk. The maintainers are not responsible for any damage to your device resulting from firmware updates.

## Contributing

If you encounter issues or have improvements, please:
1. Open an [Issue](../../issues) to report problems
2. Share your experience with the community
3. Help others who may have questions

## Sharing

Please share this repository with others who want MIDI functionality on their Gigcaster 8!

## Support

For device-specific support, please contact:
- Roland Support: [Roland Support Website](https://www.roland.com/us/support/)
- Boss Support: [Boss Support Website](https://www.boss.info/us/support/)

---

**Note**: This is a community-maintained firmware update. It is not officially supported by Roland/Boss.
