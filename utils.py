import cv2
import scipy.stats as stats
import numpy as np


def function_binary(imagePath, inputValue, savePath):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, inputValue, 255, cv2.THRESH_BINARY)
    cv2.imwrite(savePath, img)
    
    
def function_normalize(imagePath, savePath):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    
    test_img = np.where(img == 0, np.NAN, img)
    x_median = np.nanmedian(test_img, axis=1)
    x_std = np.nanstd(test_img, axis=1)
    x_median_nan = np.nan_to_num(x_median, nan=0)
    x_std_nan = np.nan_to_num(x_std, nan=1)
    z_score = (img - x_median_nan.reshape(-1, 1)) / (
        x_std_nan.reshape(-1, 1) + 1e-6
    )
    zscore_scaled = (
        ((z_score - np.min(z_score)) / (np.max(z_score) - np.min(z_score))) * 255
    ).astype(np.uint8)
    
    cv2.imwrite(savePath, zscore_scaled)
    
    
def function_adthreshold(imagePath, inputValue, savePath):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, inputValue, 2)
    cv2.imwrite(savePath, img)
    
    
def function_blob(imagePath, inputValue, savePath):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    contours, hier = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    
    for contour in contours:
        contourArea = cv2.contourArea(contour)
        if contourArea >= inputValue:
            cv2.drawContours(img, [contour], -1, (36, 255, 12), 1)
    
    cv2.imwrite(savePath, img)
    

def function_blur(imagePath, inputWidthValue, inputHeightValue, inputSigmaValue, savePath):
    img = cv2.imread(imagePath)
    img = cv2.GaussianBlur(img, (inputWidthValue, inputHeightValue), inputSigmaValue)
    cv2.imwrite(savePath, img)