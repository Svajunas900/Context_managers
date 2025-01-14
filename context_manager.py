class RemoveNonUnicodeCharacters:

  def __init__(self, file_path, new_file_path):
      self.file_path = file_path
      self.new_file_path = new_file_path
      self.original_content = None
      self.new_content = None

  def __enter__(self):
      with open(self.file_path, 'r', encoding="utf8") as file:
        self.original_content = file.read()
      string_encode = self.original_content.encode("ascii", "ignore")
      string_decode = string_encode.decode()
      string_list = string_decode.split()
      result = []
      for word in string_list:
        if len(word) > 70:
          continue
        else:
          result.append(word)
      self.new_content = " ".join(result)
      return self.new_content

  def __exit__(self, exc_type, exc_val, exc_tb):
      with open(self.new_file_path, 'w') as file:
        file.write(self.new_content)
      

textfile = RemoveNonUnicodeCharacters("simple.txt", "new_text.txt")
with textfile as txt:
    print(txt)