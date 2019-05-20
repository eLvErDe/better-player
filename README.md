# Description

Open filename passed as argument but first check if there is an alternative with better extension:
  * .avi replaced by .mp4
  * .bmp replaced by .jpeg

Integrate nicely with Windows:
  * Use os.startfile to use Windows file associations
  * Display errors in GUI error box

# Compile as Windows binary

```
python -m pip install pyinstaller
python -m PyInstaller --onefile --noconsole better_player.py
```

Resulting exe file will be generated in `dist/` and is obviously dependent on the Python architecture you used during build.
If you want something portable, make sure to build it with 32 Bits Python distribution.

You can override `python` in commands above to use alternative Python interpreter.

If your antivirus detect the binary as Virus file, use ![upx](https://github.com/upx/upx "UPX") to repack the binary.
