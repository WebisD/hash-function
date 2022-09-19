class Hash:
   def __init__(self, text, sha256, md5):
      self.text = text
      self.sha256 = sha256
      self.md5 = md5

def get_data():

    texts = []

    file = open("data.txt", 'r')
    for line in file.readlines():
        line = line.strip()
        line = line.split(';')
        texts.append(Hash(line[0], line[1], line[2]))

    return texts