import qrcode

img = qrcode.make("https://www.pexels.com/@beankurt/")
img.save("BeanKurt Pexels QR.jpg")