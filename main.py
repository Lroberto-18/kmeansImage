import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def load_image(image_path, resize=None):
    image = Image.open(image_path)
    if resize:
        image = image.resize(resize)
    return np.array(image)


def segment_image(pixels, k, image_shape):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pixels)
    segmented_pixels = kmeans.cluster_centers_[kmeans.labels_]
    return segmented_pixels.reshape(image_shape).astype(np.uint8), kmeans


def calculate_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return float("inf")
    max_pixel = 255.0
    return 20 * np.log10(max_pixel / np.sqrt(mse))


def calculate_compression_ratio(original_size, k, num_pixels):
    bits_per_pixel = np.ceil(np.log2(k))
    compressed_size = (
        bits_per_pixel * num_pixels + k * 3 * 8
    ) / 8
    return original_size / compressed_size


def main():
    image_path = "image_1.png"
    image_np = load_image(
        image_path, resize=(256, 256)
    )
    pixels = image_np.reshape(-1, 3)
    original_size = os.path.getsize(image_path)
    num_pixels = pixels.shape[0]
    k_values = list(range(2, 11))
    segmented_images = []
    psnr_values = []
    compression_ratios = []

    for k in k_values:
        segmented_img, _ = segment_image(pixels, k, image_np.shape)
        psnr = calculate_psnr(image_np, segmented_img)
        compression_ratio = calculate_compression_ratio(original_size, k, num_pixels)
        segmented_images.append(segmented_img)
        psnr_values.append(psnr)
        compression_ratios.append(compression_ratio)

    num_images = len(k_values) + 1
    rows = 2
    cols = (num_images + 1) // rows
    plt.figure(figsize=(15, 8))
    for i, (segmented_img, k, psnr, comp_ratio) in enumerate(
        zip(segmented_images, k_values, psnr_values, compression_ratios), start=1
    ):
        plt.subplot(rows, cols, i)
        plt.imshow(segmented_img)
        plt.title(f"K = {k}\nPSNR: {psnr:.2f} dB\nCompressão: {comp_ratio:.2f}x")
        plt.axis("off")

    plt.subplot(rows, cols, num_images)
    plt.imshow(image_np)
    plt.title("Imagem Original")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()