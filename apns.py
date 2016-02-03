
import socket, ssl, json
from struct import pack
from binascii import a2b_hex

class APNS(object):

    def __init__(self, is_prod=False):

        if (is_prod is True):
            self._address = ( 'gateway.push.apple.com', 2195 )
            self._cert = 'keys/skirmish_prod_cert.pem'
            self._key = 'keys/skirmish_prod_key.pem'
        else:
            self._address = ( 'gateway.sandbox.push.apple.com', 2195 )
            self._cert = 'keys/skirmish_dev_cert.pem'
            self._key = 'keys/skirmish_dev_key_np.pem'


    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connection = ssl.wrap_socket(s,self._key,self._cert)
        self._connection.connect(self._address)

    def disconnect(self):
        self._connection.close()

    def send(self, token_hex, payload):
        token_bin = a2b_hex(token_hex)
        token_length = pack('>H', len(token_bin))

        # payload = {"apn": payload, "content-available": 1}
        payload = {
            "content-available": 1,
            "apn": payload,
            "aps" : { "alert" : u"Нотификашка" },
            "acme2" : [ "bang",  "whiz" ]
        }

        payload_json = json.dumps(payload, separators=(',',':'), ensure_ascii=False).encode('utf-8')
        payload_length_bin = pack('>H', len(payload_json))

        zero_byte = '\0'
        zero_byte = bytes(zero_byte, 'utf-8')

        notification = (zero_byte + token_length + token_bin + payload_length_bin + payload_json)

        self._connection.write(notification)