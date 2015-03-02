from Crypto.PublicKey import RSA 

class RSAwrapper():
  
  def keygen(self):
    key = RSA.generate(2048, e=65537) 
    public = key.publickey().exportKey("PEM") 
    private = key.exportKey("PEM") 
    print public
    print private

if __name__ == '__main__':
  try:
    rsa = RSAwrapper()
    rsa.keygen()
  except:
    print "error"
