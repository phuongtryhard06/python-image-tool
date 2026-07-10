from image_tools.resize.resize_images import resize_images

if __name__ == "__main__":

    # ==============================  resize image ==============================
    input_dir = "input_images/resize/web_mqtt_image"
    output_dir = "output_images/resize/web_mqtt_image"
    width = 90
    height = 80

    resize_images(input_dir, output_dir, width, height)

    # another tool can be added here in the future