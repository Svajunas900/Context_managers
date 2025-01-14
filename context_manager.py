class RemoveNonUnicodeCharacters:

  def __init__(self, original_content, new_file_path):
      self.new_file_path = new_file_path
      self.original_content = original_content
      self.new_content = None
      self.first_five_words = []

  def __enter__(self):
      string_encode = self.original_content.encode("ascii", "ignore")
      string_decode = string_encode.decode()
      string_list = string_decode.split()
      result = []
      for word in string_list:
        if len(word) > 70:
          continue
        else:
          result.append(word)
      self.first_five_words = result[0:5]
      self.new_content = " ".join(result)
      return " ".join(self.first_five_words)

  def __exit__(self, exc_type, exc_val, exc_tb):
      with open(self.new_file_path, 'w') as file:
        file.write(self.new_content)
      