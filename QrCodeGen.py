import qrcode

def QrCodeGen(text):
  img = qrcode.make(text)
  type(img)  # qrcode.image.pil.PilImage
  img.save("url.png")
  return img

#todo make it into SaaS

#step 1: UI on website
#step 2: insert the url / text
#step 3: generate the qr code
#step 4: upload the qr code to the website
#step 5: download the qr code
#step 6: share the qr code

