# -*- coding: utf-8 -*-
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(os.path.join(__file__)))

LANGUAGE = 'cs'

def get_gettext(lang):
    import gettext
    path =  os.path.join(PROJECT_ROOT, 'locale')
    t = gettext.translation('messages', path, languages=[lang],
                            codeset='utf8')
    t.install()

    return lambda message: t.gettext(message).decode('utf-8')

try:
    lang = os.environ.get("INVOICE_LANG", LANGUAGE)
    _ = get_gettext(lang)
except IOError:
    _ = lambda x: x
    print("Fix this!")
except ImportError:
    _ = lambda x: x

FONT_PATH = os.path.join(PROJECT_ROOT, "fonts", "DejaVuSans.ttf")
FONT_BOLD_PATH = os.path.join(PROJECT_ROOT, "fonts", "DejaVuSans-Bold.ttf")

if not os.path.isfile(FONT_PATH):
    FONT_PATH = "/usr/share/fonts/TTF/DejaVuSans.ttf"
    FONT_BOLD_PATH = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"

if not os.path.isfile(FONT_PATH):
    raise Exception("Fonts not found")
