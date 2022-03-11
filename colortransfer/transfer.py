import numpy as np
import cv2 as cv


def transfer_color(source_image: np.ndarray, target_image: np.ndarray) -> np.ndarray:
    """Color transfer between images

    Args:
        source_image (np.ndarray): Color source image
        target_image (np.ndarray): Target image

    Returns:
        np.ndarray: The result of the color transfer

    Reference:
        doi: 10.1109/38.946629
    """
    # RGB -> L*a*b*
    src_img = cv.cvtColor(source_image, cv.COLOR_RGB2Lab)
    dst_img = cv.cvtColor(target_image, cv.COLOR_RGB2Lab)

    # Calculate mean and std
    src_means, src_stds = src_img.mean(axis=(0, 1)), src_img.std(axis=(0, 1))
    dst_means, dst_stds = dst_img.mean(axis=(0, 1)), dst_img.std(axis=(0, 1))

    # Transfer
    dst_img = dst_img - dst_means.reshape((1, 1, 3))
    dst_img *= (dst_stds / src_stds).reshape((1, 1, 3))
    dst_img += src_means.reshape((1, 1, 3))

    # L*a*b* -> RGB
    dst_img = np.clip(dst_img, 0, 255).astype(np.uint8)
    dst_img = cv.cvtColor(dst_img, cv.COLOR_LAB2RGB)
    return dst_img
