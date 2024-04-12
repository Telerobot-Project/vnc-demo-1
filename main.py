from lib.video import Video
from lib.ui import *
from lib.robot import Robot

window = Window(378 * 2, 672, "TeleBOT")
robot = Robot()
user_video = Video(window)
usb_video = Video(window, (1280, 720))
tof_video = Video(window)
joystick = Joystick(378 + 89 + 100, 370 + 100, 100, 20, (217, 217, 217), window)
left_turn_btn = Button(378 + 29, 350, 40, 40, (217, 217, 217), window)
right_turn_btn = Button(378 + 309, 350, 40, 40, (217, 217, 217), window)

window.start()
usb_video.start()
robot.start()

while True:
    window.read()
    if not window.run:
        break
    usb_video.read()
    joystick.read()
    left_turn_btn.read()
    right_turn_btn.read()

    robot.direction = joystick.angle;
    robot.speed = joystick.distance / joystick.r1 * robot.max_speed
    robot.turn_speed = -30 if left_turn_btn.down else 30 if right_turn_btn.down else 0

    window.fill((34, 34, 34))
    usb_video.draw(0, 0, 378, 672)
    tof_video.draw(378 + 29, 28, 320, 240)
    joystick.draw()
    left_turn_btn.draw()
    right_turn_btn.draw()
    window.update()

print('Closing')
robot.close()
usb_video.close()
