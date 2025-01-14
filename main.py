from fastapi import FastAPI
import json
from selenium_scraper import write_text_from_wiki
from context_manager import RemoveNonUnicodeCharacters


app = FastAPI()


@app.get("/{user_text}")
def home(user_text: str):
  write_text_from_wiki(user_text, f"User_text_{user_text}.txt")
  with open(f"User_text_{user_text}.txt", encoding="utf8") as file:
    wiki_text = file.read()
  text_file = RemoveNonUnicodeCharacters(wiki_text, f"New_text_{user_text}.txt")
  with text_file as text:
    response = json.dumps({"Text Found": text})
  return response