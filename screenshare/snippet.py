import PIL
from PIL import Image, ImageGrab, ImageDraw
from screeninfo import get_monitors
import time
import io
import pyautogui

screen = 1
screenbounds = None

def getScreenBounds():
    monitors = get_monitors()
    if monitors == None:
        raise Exception("get_monitors return None")

    print(f"Calibrating! Monitors is {monitors}")

    screenBounds = None
    if screen >= 0 and screen < len(monitors):
        mon = monitors[screen]
        screenBounds = (mon.x, mon.y, mon.x +
                        mon.width, mon.y + mon.height)

    if screenBounds == None:
        minX = min((mon.x for mon in monitors))
        minY = min((mon.y for mon in monitors))
        maxX = max((mon.x + mon.width for mon in monitors))
        maxY = max((mon.y + mon.height for mon in monitors))
        screenBounds = (minX, minY, maxX, maxY)
    return screenBounds

def setScreen(sc):
    global screen, screenbounds

    screen = sc
    screenbounds = getScreenBounds()

def Snippet(heightRes):
    if screenbounds == None:
        setScreen(screen)

    #bounds = getScreenBounds()
    bounds = screenbounds

    im = ImageGrab.grab(bbox=bounds, all_screens=True)
    pos = pyautogui.position()

    if pos.x >= bounds[0] and pos.x < bounds[2] and pos.y >= bounds[1] \
        and pos.y < bounds[3]:

        draw = ImageDraw.Draw(im)

        x = pos.x - bounds[0]
        y = pos.y - bounds[1]

        draw.ellipse([(x - 10, y - 10), (x + 10, y + 10)], outline="#ff0000cc", width=3)

    #print(f"Cursor pos: {pos}")

    if heightRes < -1:
        print(f"Natural dimensions are {im.width}, {im.height}")
        heightRes = -1

    if heightRes != -1:
        aspect = im.width / im.height
        im = im.resize((int(aspect * heightRes), heightRes), resample=PIL.Image.NEAREST)

    data = io.BytesIO()
    im.save(data, format="PNG")

    #print(data.getvalue())
    return data.getvalue()

