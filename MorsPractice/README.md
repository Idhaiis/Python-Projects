# Morse Code Keyboard Translator

A Python script that translates keyboard inputs into Morse code based on key press duration.

## Setup
Install the required library:
```bash
pip install keyboard
```
*Note: Run the script with administrative privileges (Run as Admin/sudo) as it hooks into keyboard events.*

## Usage
Run the script:
```bash
python main.py
```

* **Dot (`.`):** Tap any key briefly (<= 0.1 seconds).
* **Dash (`_`):** Hold any key (> 0.1 seconds).
* **Confirm Character:** Press `Enter`.
* **Exit:** Press `Esc`.
