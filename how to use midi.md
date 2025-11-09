# GCS-8 MIDI Integration Tutorial (Firmware v1.1 Upgrade)

## 1. Enabling MIDI on Your GCS-8

### Step 1: Go to Settings → MIDI

You'll see the following menu entries:

- **Enable MIDI** – Off by default
- **MIDI Role** – Device / Host / Both
- **Active Profile** – Select which MIDI mapping you want
- **MIDI Status** – Shows connection info

### Step 2: Tap Enable MIDI → ON

- The screen will briefly say "Starting MIDI Router…"
- The USB port will re-enumerate.
- Your computer (or external controller) should now detect a device called **GCS8 MIDI**.

### Step 3: Choose MIDI Role

- **Device Mode** – The GCS-8 appears as a USB-MIDI device to your DAW (Ableton, Logic, etc.).
- **Host Mode** – Lets you plug in a USB-MIDI controller (keyboard, knob box, etc.) directly into the GCS-8.
- **Both Mode** – The GCS-8 acts as a bridge between DAW and controller (advanced users).

---

## 2. Using External Controllers

### Step 1: Connect your MIDI device

- If your GCS-8 is in **Host** or **Both** mode, plug your controller into the USB port.
- If in **Device** mode, connect the GCS-8 to your computer via USB-C.

### Step 2: Check Settings → MIDI → Status

You'll see something like:

```
Connected MIDI devices:
 - Novation Launch Control XL (Host)
 - Ableton Live (Device)
Incoming activity: OK
```

### Step 3: Press the Home button → Tap MIDI Tools

Here you'll find three main utilities:

- **MIDI Learn**
- **MIDI Mappings**
- **MIDI Monitor**

---

## 3. Assigning Controls (MIDI Learn)

### Step 1: Open MIDI Tools → MIDI Learn

The screen will show:

```
Touch or move a control on your external MIDI device
Then select the function you want to control
```

### Step 2: Move a knob, fader, or pad on your MIDI controller.

You'll see:

```
> Detected: CC74 (Channel 1, Value 0–127)
```

### Step 3: Choose the destination parameter

Use the touchscreen to pick what that control should move:

```
Assign to → Channel 1 Gain
Tap Save Mapping 
```

That mapping is now stored in the active profile (e.g., Default).

---

## 4. Viewing & Editing Mappings

Go to **MIDI Tools → MIDI Mappings**

Here you'll see all active links:

| Source (MIDI) | Destination (Parameter) | Notes |
|---------------|------------------------|-------|
| CC74 (CH1) | Channel 1 Gain | — |
| CC1 (CH1) | Reverb Level | Foot Pedal |
| Note 60 | Sound Pad #3 Trigger | — |

Tap any mapping to edit, delete, or re-assign.

You can also tap **Export** to save this profile to microSD, or **Import** to load from USB.

---

## 5. Advanced Tips

### a. Dual Role (Bridge Mode)

If **MIDI Role = Both**, you can pass data between the external controller and your DAW via the GCS-8.

**Example:**

- Fader on your controller → adjusts channel gain on GCS-8
- DAW automation → sends MIDI CC back → GCS-8 motorizes virtual fader

### b. Profile Management

Profiles are stored at:

```
/etc/gcs8/midi_profiles/
```

Each one is a JSON file:

```json
{
  "name": "Default",
  "mappings": [
    { "cc": 74, "channel": 1, "target": "mixer.channel.1.gain", "scale": [0.0, 1.0] },
    { "cc": 1, "channel": 1, "target": "effects.reverb.level" }
  ]
}
```

You can edit or create new profiles via **Settings → MIDI → Active Profile → New Profile**.

---

## 6. Monitoring & Troubleshooting

### Step 1: Open MIDI Tools → MIDI Monitor

You'll see live traffic:

```
<-- CC74 ch1 val 83
<-- CC1 ch1 val 120
--> CC10 ch1 val 45 (feedback)
```

### Step 2: If you don't see messages:

- Check **"Enable MIDI"** is ON.
- Ensure USB cable supports data (not charge-only).
- If connected to PC, verify **"GCS8 MIDI"** appears under MIDI devices in your DAW.
- Restart MIDI service (**Settings → MIDI → Restart**).

---

## 7. External Use Example (Ableton Live)

1. Connect GCS-8 via USB-C.

2. In **Ableton Preferences → MIDI**:
   - **Input:** GCS8 MIDI
   - **Output:** GCS8 MIDI

3. Move a fader or pad — Ableton should show MIDI activity.

4. Assign it to a control in Ableton, or use the GCS-8 Learn mode to bind Ableton CCs to mixer channels.

---

## 8. Developer Notes (for Advanced Users)

- **IPC socket for router:** `/var/run/gcs8-midi.sock`

- **JSON commands (examples):**

```bash
echo '{"cmd":"status"}' | nc -U /var/run/gcs8-midi.sock
echo '{"cmd":"set_profile","name":"Studio"}' | nc -U /var/run/gcs8-midi.sock
```

- Profiles editable manually or via UI.
- To disable MIDI entirely: `systemctl stop gcs8-midi-router`.

---

## 9. Summary

| Action | Where |
|--------|-------|
| Enable / Disable MIDI | Settings → MIDI |
| Choose Device/Host/Both | Settings → MIDI Role |
| Learn new control | MIDI Tools → MIDI Learn |
| View/Edit profiles | MIDI Tools → Mappings |
| Monitor MIDI data | MIDI Tools → Monitor |

