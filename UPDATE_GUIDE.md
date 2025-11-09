# Gigcaster 8 Firmware Update - Step-by-Step Guide

## Pre-Update Checklist

- [ ] Current firmware version checked on device
- [ ] USB cable that supports data transfer ready
- [ ] Computer with USB 2.0 or 3.0 port available
- [ ] Firmware files extracted and verified
- [ ] Stable power supply ensured
- [ ] All USB applications closed

## Update Process

### Step 1: Check Current Firmware Version

1. Power on your Gigcaster 8
2. Touch the **MENU** icon on the home screen
3. Select **SETUP**
4. Select **GENERAL**
5. Note the current firmware version displayed under "VERSION"
6. **Record it here:** ________________

### Step 2: Prepare Device for Update

1. **Turn OFF** your Gigcaster 8
2. **Press and HOLD** the **[MARK]** button
3. While holding [MARK], **turn ON** the power
4. Keep holding [MARK] until screen displays **"PREPARING..."**
5. Release [MARK] button
6. Screen should show **"PREPARING..."** then **"CONNECTED"**

### Step 3: Connect to Computer

1. Connect Gigcaster 8 to your computer using USB cable
2. Wait for device to be recognized
3. On Mac: Device should appear as **"GCS-8_INT"** drive
4. On Windows: Device should appear as removable drive

### Step 4: Transfer Firmware Files

**CRITICAL:** Files MUST be at the root level of the drive (not in any subfolder)

1. Open the **GCS-8_INT** drive
2. Navigate to: `/Users/aiecan/Downloads/midi firmware gigcaster/firmware/`
3. **Select ALL firmware files** (excluding README.md and .json files)
4. Copy files to the **root** of the GCS-8_INT drive
5. Verify files are copied (not in a subfolder)
6. **Safely eject** the GCS-8_INT drive from your computer

### Step 5: Initiate Update

1. After ejecting, Gigcaster 8 screen should display **"UPDATE ?"**
2. Press the **[REC]** button to confirm
3. Screen will show **"WRITING..."**
4. **DO NOT** power off or disconnect during this process
5. Wait for screen to display **"COMPLETE"**

### Step 6: Complete Update

1. When "COMPLETE" appears, **turn OFF** the Gigcaster 8
2. Wait 5 seconds
3. **Turn ON** the Gigcaster 8 normally
4. Device should boot with new firmware

### Step 7: Verify Update

1. Power on Gigcaster 8
2. Touch **MENU** → **SETUP** → **GENERAL**
3. Check firmware version - should show **gcs8_sys_v105**
4. Test device functions:
   - [ ] Audio input/output
   - [ ] Streaming functions
   - [ ] Menu navigation
   - [ ] All buttons and controls

## Important Warnings

⚠️ **CRITICAL:** Do NOT power off during update process
⚠️ **CRITICAL:** Do NOT disconnect USB cable during update
⚠️ **CRITICAL:** Ensure files are at root level (not in subfolders)
⚠️ Ensure stable power supply throughout process

## Troubleshooting

### Device Not Detected
- Try different USB cable
- Try different USB port
- Restart device in update mode (hold MARK while powering on)
- Check USB drivers

### Update Fails
- Verify files are at root of GCS-8_INT drive
- Re-extract firmware files
- Ensure all files copied completely
- Try re-downloading firmware from Roland

### After Update Issues
- Power cycle device (off/on)
- Check for error messages
- Contact Roland support if problems persist

## Support

- [Roland Support](https://www.roland.com/us/support/)
- [Gigcaster 8 Updates](https://www.roland.com/us/support/by_product/gigcaster/updates_drivers/)
- [Update Guide](https://support.roland.com/hc/en-us/articles/14860520347803-Gigcaster-8-How-to-update-system-program-firmware)

