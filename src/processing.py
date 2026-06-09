import cv2
import numpy as np

# --- Threshold Configurations ---
LOWER_RED_1 = np.array([0, 50, 50])
UPPER_RED_1 = np.array([10, 255, 255])
LOWER_RED_2 = np.array([170, 50, 50])
UPPER_RED_2 = np.array([180, 255, 255])

SEN = 100
LOWER_W = np.array([0, 0, 255 - SEN], dtype=np.uint8)
UPPER_W = np.array([179, SEN, 255], dtype=np.uint8)

def process_cavity_image(image_path, is_dark_mode=False):
    """
    Processes a thermal image to locate defects/hotspots via HSV color masks.
    Returns the final concatenated NumPy array (Original + Processed).
    """
    img = cv2.imread(image_path)
    if img is None:
        return None

    im = cv2.resize(img, (500, 500))
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    
    mask0 = cv2.inRange(hsv, LOWER_RED_1, UPPER_RED_1)
    mask1 = cv2.inRange(hsv, LOWER_RED_2, UPPER_RED_2)
    mask_w = cv2.inRange(hsv, LOWER_W, UPPER_W)
    
    mask = mask0 + mask1 + mask_w
    cr_mask = mask[40:460, 0:475]

    res = cv2.bitwise_and(im, im, mask=mask)
    contours, _ = cv2.findContours(cr_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    min_area = 600 if is_dark_mode else 700
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            moment = cv2.moments(contour)
            if moment['m00'] != 0:
                cx = int(moment['m10'] / moment['m00'])
                cy = int(moment['m01'] / moment['m00'])
            else:
                cx, cy = 0, 0

            [x, y, w, h] = cv2.boundingRect(contour)
            cv2.rectangle(res, (x, y + 40), (w + x, h + y + 40), (0, 255, 0), 2)
            
            # Dynamic text placement math matching runtime theme status
            text_y = cy - 20 if is_dark_mode else y + 25
            text_x = cx - 30 if is_dark_mode else int(x + w / 2 - 25)
            cv2.putText(res, "Hotspot", (text_x, text_y), 2, 0.5, (255, 255, 255), 1, 0)

    # Combine both matrices side-by-side for horizontal layout analysis
    numpy_horizontal_concat = np.concatenate((im, res), axis=1)
    return cv2.cvtColor(numpy_horizontal_concat, cv2.COLOR_BGR2RGB)