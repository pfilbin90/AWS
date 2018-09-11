import OpenSSL 
import ssl, socket 

def getSSLexpiring(): 
    cert=ssl.get_server_certificate(('www.google.com', 443)) 
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert) 
    x509.get_notAfter() 
 
def lambda_handler(event, context): 
    getnotAfter 
    print(getnotAfter.text) 
    return 