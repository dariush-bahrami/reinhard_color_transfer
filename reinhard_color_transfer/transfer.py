import cv2
import numpy as np
from PIL import Image


def transfer_color(
    source_image: Image.Image, color_image: Image.Image, alpha: float = 0.5
) -> Image.Image:
    """
    Applies a modified version of Reinhard's color transfer algorithm to transfer the color distribution
    from the `color_image` to the `source_image`.

    This function converts both input images from RGB to LAB color space, computes their respective
    means and standard deviations across each channel, and adjusts the source image's color statistics
    to more closely match those of the color image. The degree of this adjustment is controlled by the
    `alpha` parameter, enabling smooth blending between the original and the transferred colors.

    Args:
        source_image (Image.Image): The source image whose color appearance will be modified.
        color_image (Image.Image): The reference color image providing the target color statistics.
        alpha (float, optional): Blending factor between 0 and 1 (default is 0.5). A value closer to 1 gives more
            weight to the color image, while a value closer to 0 retains more of the source image's original color.

    Returns:
        Image.Image: A new image with the color appearance of the source image shifted
        towards that of the color image.

    Reference:
        doi: 10.1109/38.946629
    """
    # convert to numpy
    source_image = np.asarray(source_image.convert("RGB"))
    color_image = np.asarray(color_image.convert("RGB"))

    # Change color space to LAB
    src_lab = cv2.cvtColor(source_image, cv2.COLOR_RGB2LAB)
    clr_lab = cv2.cvtColor(color_image, cv2.COLOR_RGB2LAB)

    # Compute color transfer variables
    mu_src = np.mean(src_lab, axis=(0, 1))
    sigma_src = np.std(src_lab, axis=(0, 1))
    mu_clr = np.mean(clr_lab, axis=(0, 1))
    sigma_clr = np.std(clr_lab, axis=(0, 1))
    mu_exp = alpha * mu_clr + (1 - alpha) * mu_src
    sigma_exp = alpha * sigma_clr + (1 - alpha) * sigma_src

    # Do color transfer
    result_lab = ((src_lab - mu_src) / sigma_src) * sigma_exp + mu_exp
    result_lab = np.clip(result_lab, 0, 255).astype(np.uint8)
    result_rgb = cv2.cvtColor(result_lab, cv2.COLOR_LAB2RGB)

    # Convert back to PIL Image
    result_rgb = Image.fromarray(result_rgb)

    return result_rgb
