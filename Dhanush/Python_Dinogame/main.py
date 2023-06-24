import pyautogui
from PIL import Image, ImageGrab
import time
from numpy import asarray
import my_model
from PIL import Image
from pytesseract import pytesseract
import numpy as np

move = 'none'

def crop_image():
     # Opens a image in RGB mode
    im = Image.open(r"C:\Users\BASWA HARICHANDANA\Desktop\Dhanush\current_state.png")
    
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size
    
    # Setting the points for cropped image
    left = 600
    top = height / 3
    right = 1300
    bottom = 2 * height / 4
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im1.save('game_state.jpg')
    
    # Shows the image in image viewer
    # im1.show()

def is_gameover():
    state = False #state is current game condition
    #Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    #Define path to image
    path_to_image = 'game_state.jpg'

    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Extract text from image
    text = pytesseract.image_to_string(img) 
    path_to_text = 'game_over.jpg'
    game_over_image = Image.open(path_to_text)
    game_over = pytesseract.image_to_string(game_over_image)
    if text == game_over:
        # print('hi')
        state = True
    return state

def hit(key):
    if key == 'up':
        pyautogui.keyDown(key)
def refresh_screen():
    pyautogui.hotkey('ctrl', 'r')
    return  
    
# refresh_screen()
# time.sleep(1)
# def draw():
#     pyautogui.keyDown(key)

def takescreenshot():
    screenshot = ImageGrab.grab().convert('L')
    filepath = 'current_state.png'
    screenshot.save(filepath, 'PNG')  # Equivalent to `screenshot.save(filepath, format='PNG')

def crop_to_req_portion():
     # Opens a image in RGB mode
    im = Image.open(r"C:\Users\BASWA HARICHANDANA\Desktop\Dhanush\current_state.png")
    
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size
    
    # Setting the points for cropped image
    side = 200 #side of the square

    left = 220
    top = height / 2 +40
    right = left +  side
    bottom = top + side
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im1.save('input_image.jpg')
    # Shows the image in image viewer
    # im1.show()
def output_move(output):

    P_hit_up, P_no_action = output[0], output[1]
    if P_hit_up>=P_no_action:
        hit('up')
        move = 'up'
    else:
        return
    return
def model_output(game_state):
    if game_state == False: #we are alive
        if move == 'up':
            return [1, 0]
        else:
            return [0, 1] 
    else:                   #we are dead
        if move == 'up':
            return [0, 1]
        else:
            return [1, 0]
train_times = 1
batch_size = 1
input_data = []
output_data = []
time.sleep(4.5)

for i in range(train_times):

    for j in range(batch_size):        
        takescreenshot()
        crop_to_req_portion()
        temporary_array = my_model.predict_move()
        output, input_image = temporary_array[0], temporary_array[1]
        # print(f'This is {output}')
        output_move(output)
        time.sleep(0.5)
        takescreenshot()
        crop_image()
        game_state = is_gameover()
        if game_state == False:#we are still alive...
            input_data.append(input_image)
            output_data.append(model_output(game_state))
        else: #we are dead
            input_data.append(input_image)
            output_data.append(model_output(game_state))
            refresh_screen()
            time.sleep(1)
            hit('up')
            time.sleep(4.8)
    print("..............I came till here...........")
    my_model.model.fit(input_data, output_data, epochs=3)

#     for i in range(1):
#         time.sleep(1)
#         takescreenshot()
#     # print(asarray(image))    
# time.sleep(2)
# screenshot = takescreenshot()
# # print(screenshot.shape)
# crop_image()
# game_condition = is_gameover()
# print(game_condition)
