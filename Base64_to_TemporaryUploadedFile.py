imgcontent = request.data.get("imageBase64").split(':')[1:][0].split(';')[1].split(',')[1]
img = Image.open(io.BytesIO(base64.b64decode(imgcontent)))
img.convert('RGB')
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format="PNG")