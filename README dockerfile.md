# image-resizer

Resizes images to 1280x800 (center crop).

## Run

docker run -v /path/to/your/images:/data image-resizer python image-resizer.py /data/yourimage.jpg

Output will be saved as yourimage_fixed.png in the same folder.
