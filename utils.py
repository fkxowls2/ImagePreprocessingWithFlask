import cv2
import scipy.stats as stats
import numpy as np


def function_binary(imagePath, inputValue, savePath):
    img = cv2.imread(imagePath)
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