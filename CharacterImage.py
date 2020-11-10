import cv2

def sort_contours(cnts,reverse = False):
    i = 0
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes), key=lambda b: b[1][i], reverse=reverse))
    return cnts

def getCharactersFromImage(plate_image):
    cont, _  = cv2.findContours(plate_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    test_roi = plate_image.copy()
    crop_characters = []
    digit_w, digit_h = 45, 90

    for c in sort_contours(cont):
        (x, y, w, h) = cv2.boundingRect(c)
        ratio = h/w
        if 1<=ratio<=3.5: # Only select contour with defined ratio
            if h/plate_image.shape[0]>=0.5: # Select contour which has the height larger than 50% of the plate
                # Draw bounding box arroung digit number
                cv2.rectangle(test_roi, (x, y), (x + w, y + h), (0, 255,0), 2)

                # Sperate number and gibe prediction
                curr_num = plate_image[y:y+h,x:x+w]
                curr_num = cv2.resize(curr_num, dsize=(digit_w, digit_h))
                _, curr_num = cv2.threshold(curr_num, 220, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                crop_characters.append(curr_num)
                
    crop_characters_with_border = []
    for character in crop_characters:
        characterImage = cv2.copyMakeBorder(
            character,
            top=0,
            bottom=0,
            left=5,
            right=5,
            borderType=cv2.BORDER_CONSTANT,
            value=[0,0,0]
        )
        characterImage = cv2.bitwise_not(characterImage)
        crop_characters_with_border.append(characterImage)

    concatedCharacters = cv2.hconcat(crop_characters_with_border)
    concatedCharacters = cv2.bitwise_not(concatedCharacters)
        
    return concatedCharacters