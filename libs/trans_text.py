from googletrans import Translator

# translates the text string given the source and destination languages
def trans_text(text_string,lang_dest,lang_source):
    translator = Translator()
    text_string = translator.translate(text_string, dest=lang_dest, src=lang_source).text
    return text_string