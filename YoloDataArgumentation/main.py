import os
import os

import cv2

from DataArgumentation.DataArgumentationImplements import ImageAugmentations  # Thay your_module bằng tên module của bạn
from configs.dataIO import InputObject  # Giả định bạn đã định nghĩa các class này


def main():
    # Tạo thư mục để lưu kết quả nếu nó chưa tồn tại
    output_dir = 'TestedResult'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Tải ảnh đầu vào
    image_path = 'images.jpg'
    image = cv2.imread(image_path)

    # Khởi tạo đối tượng ImageAugmentations
    augmentations = ImageAugmentations()

    # Thực hiện các phương thức augmentations và lưu kết quả
    # Flip
    config_flip = InputObject(image=image, mode=0)  # Vertical flip
    output_flip = augmentations.flip(config_flip)
    # output_flip.to_image(os.path.join(output_dir, 'flipped_vertical.jpg'))
    cv2.imwrite(os.path.join(output_dir, 'flipped_vertical.jpg'), output_flip.result)

    config_flip.mode = 1  # Horizontal flip
    output_flip = augmentations.flip(config_flip)
    cv2.imwrite(os.path.join(output_dir, 'flipped_horizontal.jpg'), output_flip.result)

    config_flip.mode = -1  # Both dimensions flip
    output_flip = augmentations.flip(config_flip)
    cv2.imwrite(os.path.join(output_dir, 'flipped_both.jpg'), output_flip.result)

    # Rotate image
    config_rotate = InputObject(image=image, angle=45, scale=1.0)
    output_rotate = augmentations.rotate_image(config_rotate)
    cv2.imwrite(os.path.join(output_dir, 'rotated_image.jpg'), output_rotate.result)

    # Resize image
    config_resize = InputObject(image=image, width=300, height=300)
    output_resize = augmentations.resize(config_resize)
    cv2.imwrite(os.path.join(output_dir, 'resized_image.jpg'), output_resize.result)

    # Crop image
    config_crop = InputObject(image=image, crop_size=100, num_crops=5)
    output_crop = augmentations.crop(config_crop)
    cv2.imwrite(os.path.join(output_dir, 'cropped_image.jpg'), output_crop.result)

    # Color Jitter
    config_color_jitter = InputObject(image=image, brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1)
    output_color_jitter = augmentations.color_jitter(config_color_jitter)
    cv2.imwrite(os.path.join(output_dir, 'color_jittered_image.jpg'), output_color_jitter.result)

    # Gaussian Blur
    config_gaussian_blur = InputObject(image=image, kernel_size=5)
    output_gaussian_blur = augmentations.gaussian_blur(config_gaussian_blur)
    cv2.imwrite(os.path.join(output_dir, 'gaussian_blurred_image.jpg'), output_gaussian_blur.result)

    print("All augmentations have been applied and saved in the 'TestedResult' directory.")


if __name__ == "__main__":
    main()
