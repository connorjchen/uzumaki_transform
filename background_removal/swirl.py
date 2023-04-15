import numpy as np
import cv2
from skimage.transform import swirl
from PIL import Image

def swirl_image(image_path):
    img = cv2.imread(image_path)

    # get dimensions
    h, w = img.shape[:2]

    # get center
    cx = w//2
    cy = h//2

    # set amount, number of frames and delay
    max_amount = 20
    dist = min(h,w)/2
    angle = 50
    num_frames = 50
    delay = 50


    frames = []
    # loop and increase swirl
    for i in range(0,num_frames):

        # compute phase to increment over 360 degree for number of frames specified so makes full cycle
        amount = i*max_amount/num_frames

        # do swirl
        result = swirl(img, center=(cx,cy), rotation=angle, strength=amount, radius=dist, preserve_range=True).astype(np.uint8)

        # show result
        # cv2.imshow('result', result)
        # cv2.waitKey(delay)

        # convert to PIL format and save frames
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        pil_result = Image.fromarray(result)
        frames.append(pil_result)

    # loop and decrease swirl
    for i in range(0,num_frames):

        # compute phase to increment over 360 degree for number of frames specified so makes full cycle
        amount = (num_frames-i)*max_amount/num_frames

        # do swirl
        result = swirl(img, center=(cx,cy), rotation=angle, strength=amount, radius=dist, preserve_range=True).astype(np.uint8)
            
        # show result
        # cv2.imshow('result', result)
        # cv2.waitKey(delay)

        # convert to PIL format and save frames
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        pil_result = Image.fromarray(result)
        frames.append(pil_result)

    # remove file extension from image_path
    image_path = image_path.split('.')[0]

    # write animated gif from frames using PIL
    frames[0].save(f"{image_path}_swirl.gif", save_all=True, append_images=frames[1:], optimize=False, duration=delay, loop=0)