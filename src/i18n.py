_translations = {}
_current_lang = 'en'
specter = None

def load_language():
    global _translations
    lang_code = get_current_lang()
    _translations.clear()
    print("Loading language: "+lang_code)
    try:
        # Using frozen modules instead of file system
        mod = __import__('lang_' + lang_code)
        _translations.update(mod.translations)
        _current_lang = lang_code
        print("Loaded language: {}".format(lang_code))
    except ImportError:
        print("Warning: Language ("+lang_code+") not found, using English")
        _translations.clear()

def get_current_lang():
    return specter.GLOBAL.get("language", "en") if specter else "en"

def get_available_languages():
    """Returns list of available languages by discovering lang_*.py files"""
    # Start with English as it's our default/fallback
    languages = [("en", "English")]
    
    # List of language codes to try (German, Spanish, Hindi, Arabic)
    pot_lang_codes = ["de", "es", "hi", "ar"]
    
    for code in pot_lang_codes:
        try:
            mod = __import__('lang_' + code)
            # Use LANGUAGE_NAME from module if available, otherwise capitalize code
            lang_name = getattr(mod, 'LANGUAGE_NAME', code.upper())
            languages.append((code, lang_name))
        except ImportError:
            continue
        except Exception as e:
            print("Warning loading language ("+code+"): "+ e)
    
    return sorted(languages)  # Sort alphabetically by language code

def t(t_id):
    if t_id not in _translations:
        print("Warning: missing translation for '{}' in language {}".format(t_id, _current_lang))
    translation =_translations.get(t_id, t_id )
    print("Translation("+_current_lang+") for "+t_id+"): "+ translation)
    return _translations.get(t_id, t_id)
