"""
QRCode Sample
"""
import qrcode

QR = qrcode.QRCode(version=3,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=2)

QR.add_data("TEST SAMPLE QRCODE")
QR.make(fit=True)
IMG = QR.make_image()
IMG.save("TEST-QRCode.png")
IMG.show()
