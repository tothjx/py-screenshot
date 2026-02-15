# Screenshot-maker utility for gamers (python console application)

## Versions:
<pre>
VERSION DATE:           VERSION:    DESCRIPTION:
================================================================================
2026-01-31 08:40        1.2.1       init RAM-saving refactored version
--------------------------------------------------------------------------------
2026-02-15 08:45        1.2.2       embed icon and audio for screenshot
--------------------------------------------------------------------------------
</pre>

## Build:
```bash
pyinstaller --onefile screenshot.py --name=screenshot --hiddenimport=pynput.keyboard --add-data "shot.wav;." --icon=floppy.ico
```
## Download:
[screenshot.exe](https://tothj.com/download/screenshot.exe)

## Hotkeys:
F12: take a screenshot  
CTRL+END: exit
