# %%
%pip install -q pytesseract
# Note (prerequisite)- pytesseract is a library that build on Tesseract. Tesseract needs to be installed locally first  - (https://tesseract-ocr.github.io/tessdoc/Installation.html)
%pip install -q opencv-python
%pip install -q --upgrade Pillow

# %%
import pytesseract
from pytesseract import Output
from PIL import Image
import cv2



# %%

img_path1 = r"[PATH TO IMAGE]"
pytesseract.pytesseract.tesseract_cmd = r"[PATH TO tesseract.exe]"

text = pytesseract.image_to_string(img_path1,lang='eng')

''' from https://pypi.org/project/pytesseract/
image_to_string Returns unmodified output as string from Tesseract OCR processing

image_to_boxes Returns result containing recognized characters and their box boundaries

image_to_data Returns result containing box boundaries, confidences, and other information. Requires Tesseract 3.05+. For more information, please check the Tesseract TSV documentation

image_to_osd Returns result containing information about orientation and script detection.

image_to_alto_xml Returns result in the form of Tesseract’s ALTO XML format.

run_and_get_output Returns the raw output from Tesseract OCR. Gives a bit more control over the parameters that are sent to tesseract.
'''

print(text)

# %%
# Display bounding boxes (AI generated code from google search - 'pytesseract show bounding boxes')
img = cv2.imread(img_path1)
boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), img.shape[0] - int(b[2])), (int(b[3]), img.shape[0] - int(b[4])), (0, 255, 0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%



