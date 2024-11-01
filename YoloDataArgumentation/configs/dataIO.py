from typing import Optional
import numpy as np
import cv2


class InputObject:
    """
    Configuration object for augmentation operations.

    Attributes:
    - image (np.ndarray): Input image for augmentation.
    - mode (Optional[int]): Flip mode. 0 = vertical, 1 = horizontal, -1 = both.
    - angle (Optional[float]): Rotation angle in degrees.
    - scale (Optional[float]): Scale factor for rotation.
    - width (Optional[int]): Desired width for resizing.
    - height (Optional[int]): Desired height for resizing.
    - crop_size (Optional[int]): Size of square crop.
    - num_crops (Optional[int]): Number of crops.
    - brightness (Optional[float]): Brightness factor for color jitter.
    - contrast (Optional[float]): Contrast factor for color jitter.
    - saturation (Optional[float]): Saturation factor for color jitter.
    - hue (Optional[float]): Hue adjustment factor for color jitter.
    - kernel_size (Optional[int]): Kernel size for Gaussian blur.
    """

    def __init__(self,
                 image: np.ndarray,
                 mode: Optional[int] = None,
                 angle: Optional[float] = None,
                 scale: Optional[float] = 1.0,
                 width: Optional[int] = None,
                 height: Optional[int] = None,
                 crop_size: Optional[int] = None,
                 num_crops: Optional[int] = None,
                 brightness: Optional[float] = None,
                 contrast: Optional[float] = None,
                 saturation: Optional[float] = None,
                 hue: Optional[float] = None,
                 kernel_size: Optional[int] = 5):
        self.image = image
        self.mode = mode
        self.angle = angle
        self.scale = scale
        self.width = width
        self.height = height
        self.crop_size = crop_size
        self.num_crops = num_crops
        self.brightness = brightness
        self.contrast = contrast
        self.saturation = saturation
        self.hue = hue
        self.kernel_size = kernel_size


class OutputObject:
    """
    Output object for storing augmentation results.

    Attributes:
    - result (np.ndarray): Processed image.
    """

    def __init__(self, result: np.ndarray):
        self.result = result

    def to_image(self, output_path: str) -> None:
        """Save the result as an image file."""
        print(self.result)
        cv2.imwrite(output_path, self.result)