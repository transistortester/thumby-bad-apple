# Bad Apple for the Thumby
This contains the source code and supporting files to play the [Bad Apple!!](https://en.wikipedia.org/wiki/Bad_Apple!!) [music video](https://www.youtube.com/watch?v=i41KoE0iMYU&t=0s) on the [Thumby](https://thumby.us/) and [Thumby Color](https://color.thumby.us/)
### Videos:
Thumby: https://www.youtube.com/watch?v=vbBQ11BZWoU

Thumby Color: https://www.youtube.com/watch?v=cyVtrq1OPQo

## Thumby

### Real hardware
This has been added to the [Thumby Arcade](https://arcade.thumby.us), so it can be added to your thumby with a single click.

Alternatively, you can manually install it by copying the `BadApple` folder from the thumby directory of this repo to the `/Games/` folder. The video can then be selected from the games menu.

At any point during playback, pressing B will stop the video and pressing A will print memory usage (only visible if connected to a computer).
Audio can be disabled from the thumby's settings menu.

If you want to save storage space on your thumby, you can remove the audio entirely by deleting the file `badapple.zdp`.

### Emulation
Audio will not work in the emulator. Audio will be disabled automatically if emulation is detected.

If the video plays too slowly, it may be possible to speed it up by adding `usegc=False` to line 45 of `BadApple.py` (so it looks like `mvf.play(callback=callback, usegc=False)`). This will likely cause decompression errors if audio is enabled, so use with caution.

## Thumby Color

### Real hardware
This can be installed by copying the `BadApple` folder from the thumbycolor directory of this repo to the `/Games/` folder. The video can then be selected from the games menu.

At any point during playback, pressing B will stop the video and pressing A will print memory usage (only visible if connected to a computer). Pressing RB will toggle framerate display (approximate).
