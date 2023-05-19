import time
import hashlib
import qrcode
from qrcode import QRCode


def combinar_hash(string):
    """Combina un string con el tiempo actual y Devuelve un hash."""
    current_time = int(time.time())
    hasher = hashlib.md5(current_time.to_bytes() + string.encode()).hexdigest()
    return hasher


def generateQRCodesFromString(data):
    qrData = data.encode('utf-8')
    image = qrcode.make(qrData)
    return image

