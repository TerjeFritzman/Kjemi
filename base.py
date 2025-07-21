import base64
with open("static/background_image_skull.png", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read()).decode()
with open("background_image_skull.b64.txt", "w") as out_file:
    out_file.write(b64_string)