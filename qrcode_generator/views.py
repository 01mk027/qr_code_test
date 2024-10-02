from django.shortcuts import render
import qrcode 
from django.http import HttpResponse
import qrcode.constants 
from django.shortcuts import redirect

def generate_qr_code(request):
    #The URL you want the QR code to point to
    url = request.build_absolute_uri('https://kurumsal.trabzon.bel.tr/DiskapiNoDetay/419641865')

    #Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    #Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    #Convert the image to a HTTP Response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

def redirect_view(request):
    return redirect('https://www.google.com')