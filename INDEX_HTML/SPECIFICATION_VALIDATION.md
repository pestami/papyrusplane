CHAPTER ONE VALIDATION

Source: index.html

1.1 HTML Document Structure
- <!DOCTYPE html> with lang="en"
- <title> updated to "CHAPTER ONE - Thrust Pannels"
- Meta viewport set for responsive width

1.2 Chapter One Container
- Added <div id="chapter-one"> wrapper around all cockpit content
- Added .chapter-header styling with dark background and centered monospace text
- Added visible <h2>CHAPTER ONE - WLAN Controller Cockpit</h2> header

1.3 Controls and IDs (Verified)
- Slider 1 (id="slider1"): vertical range 0-100, default 50, onchange -> slider1Changed
- Slider 2 (id="slider2"): vertical range 0-100, default 50, onchange -> slider2Changed
- Button 1 (id="button1"): Engine Start -> sets Lstatus=1
- Button 2 (id="button2"): Engine Stop -> sets Lstatus=0
- Button 3 (id="button3"): Engine Start -> sets Rstatus=1
- Button 4 (id="button4"): Engine Stop -> sets Rstatus=0
- Servo slider (id="slider_server1"): horizontal range 0-180, default 0, onchange -> sliderservo1_Changed

1.4 Display Elements (Verified)
- slider1-value / slider2-value: numeric readouts
- lbl_servo1_angle: servo angle display
- Lduty, Lstatus, Rduty, Rstatus: throttle/status table cells
- tbl_servo1_angle, tbl_servo2angle: servo angle table cells
- jasonstring: concatenated status text display

1.5 Payload Behavior (sendRequestFull)
- Endpoint: POST /api/pins
- Content-Type: application/json
- JSON body keys: MOTORL_PWM (value1), MOTORL (value2), MOTORR_PWM (value3), MOTORR (value4), SERVOR (value5)
- value1 = innerHTML of Lduty
- value2 = innerHTML of Lstatus
- value3 = innerHTML of Rduty
- value4 = innerHTML of Rstatus
- value5 = innerHTML of tbl_servo1_angle
- value6 = innerHTML of tbl_servo2angle
- jasonstring format: "Lduty: {value1} ; Lstatus: {value2} ; Rduty: {value3} ; Rstatus: {value4} ; Servo1: {value5} ; Servo2: {value6}"

1.6 Event Flow (Verified)
- Any slider or button change updates its corresponding display element and calls sendRequestFull()
- Slider1Changed sets Lduty.innerText = value
- Slider2Changed sets Rduty.innerText = value
- sliderservo1_Changed sets tbl_servo1_angle.innerText = value and tbl_servo2angle.innerText = value
- button1Clicked sets Lstatus.innerText = 1
- button2Clicked sets Lstatus.innerText = 0
- button3Clicked sets Rstatus.innerText = 1
- button4Clicked sets Rstatus.innerText = 0

1.7 Chapter One Implementation Complete
- New code added: chapter-one section wrapper and chapter-header styling in index.html
- Existing cockpit functionality preserved and extended with Servo2 display linkage
