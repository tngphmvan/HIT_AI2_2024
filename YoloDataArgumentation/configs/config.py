from configs.dataIO import InputObject, OutputObject

class AugmentationsInterface:
    """
    Interface class for various image augmentation methods.

    Each method in this class applies a different type of augmentation to an input image.
    The methods accept an InputObject, which contains configuration parameters for the augmentation,
    and return an OutputObject containing the augmented image data.
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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass
