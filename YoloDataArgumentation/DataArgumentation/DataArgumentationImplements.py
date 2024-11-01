import cv2
import numpy as np
from configs.dataIO import InputObject, OutputObject
from configs.config import AugmentationsInterface  # Import the interface

class ImageAugmentations(AugmentationsInterface):
    """
    Class implementing AugmentationsInterface to apply various image augmentations.
    """

    def flip(self, config: InputObject) -> OutputObject:
        """
        Flips the image based on the specified flip mode.

        Parameters:
        - config (InputObject): Configuration object containing:
            - image (np.ndarray): The input image to flip.
            - mode (int): Flip mode, where 0 = vertical, 1 = horizontal, -1 = both axes.

        Returns:
        - OutputObject: Contains the flipped image.
        """
        if config.mode == 0:
            result = cv2.flip(config.image, 0)
        elif config.mode == 1:
            result = cv2.flip(config.image, 1)
        else:
            result = cv2.flip(config.image, -1)
        return OutputObject(result)

    def rotate_image(self, config: InputObject) -> OutputObject:
        """
        Rotates the image by the specified angle and scales it.

        Parameters:
        - config (InputObject): Configuration object containing:
            - image (np.ndarray): The input image to rotate.
            - angle (float): Rotation angle in degrees. Positive values rotate counterclockwise.
            - scale (float): Scaling factor for the image size after rotation.

        Returns:
        - OutputObject: Contains the rotated image.
        """
        (h, w) = config.image.shape[:2]
        center = (w // 2, h // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, config.angle, config.scale)
        rotated_image = cv2.warpAffine(config.image, rotation_matrix, (w, h))
        return OutputObject(rotated_image)

    def resize(self, config: InputObject) -> OutputObject:
        """
        Resizes the image to the specified width and height.

        Parameters:
        - config (InputObject): Configuration object containing:
            - image (np.ndarray): The input image to resize.
            - width (int): Target width for resizing.
            - height (int): Target height for resizing.

        Returns:
        - OutputObject: Contains the resized image.
        """
        resized_image = cv2.resize(config.image, (config.width, config.height))
        return OutputObject(resized_image)

    def crop(self, config: InputObject) -> OutputObject:
        """
        Crops random square regions from the image.

        Parameters:
        - config (InputObject): Configuration object containing:
            - image (np.ndarray): The input image to crop.
            - crop_size (int): Size of the square region to crop.
            - num_crops (int): Number of random crops to perform.

        Returns:
        - OutputObject: Contains the image with cropped regions.
        """
        h, w = config.image.shape[:2]
        masked_image = config.image.copy()

        for _ in range(config.num_crops):
            x_start = np.random.randint(0, w - config.crop_size + 1)
            y_start = np.random.randint(0, h - config.crop_size + 1)
            masked_image[y_start:y_start + config.crop_size, x_start:x_start + config.crop_size] = (0, 0, 0)

        return OutputObject(masked_image)

    def color_jitter(self, config: InputObject) -> OutputObject:
        """
        Adjusts image color properties such as brightness, contrast, saturation, and hue.

        Parameters:
        - config (InputObject): Configuration object containing:
            - image (np.ndarray): The input image to adjust.
            - brightness (float): Brightness adjustment factor.
            - contrast (float): Contrast adjustment factor.
            - saturation (float): Saturation adjustment factor.
            - hue (float): Hue adjustment factor.

        Returns:
        - OutputObject: Contains the color-adjusted image.
        """
        alpha = 1.0 + np.random.uniform(-config.contrast, config.contrast)
        beta = np.random.uniform(-config.brightness * 255, config.brightness * 255)
        jittered_image = cv2.convertScaleAbs(config.image, alpha=alpha, beta=beta)

        hsv = cv2.cvtColor(jittered_image, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[:, :, 1] *= 1 + np.random.uniform(-config.saturation, config.saturation)
        hsv[:, :, 0] += np.random.uniform(-config.hue * 180, config.hue * 180)

        hsv = np.clip(hsv, 0, 255).astype(np.uint8)
        jittered_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return OutputObject(jittered_image)

    def gaussian_blur(self, config: InputObject) -> OutputObject:
        """
        Applies Gaussian blur to the image using a specified kernel size.

        Parameters:
        - config (InputObject): Configuration object containing:
            - image (np.ndarray): The input image to blur.
            - kernel_size (int): Size of the Gaussian kernel (must be an odd integer).

        Returns:
        - OutputObject: Contains the blurred image.
        """
        blurred_image = cv2.GaussianBlur(config.image, (config.kernel_size, config.kernel_size), 0)
        return OutputObject(blurred_image)
