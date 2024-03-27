import sys
import os

locale = sys.argv[1]

os.system(f"/Library/Frameworks/Python.framework/Versions/3.10/share/doc/python3.10/examples/Tools/i18n/msgfmt.py -o "
          f"./front/assets/locales/{locale}/LC_MESSAGES/base.mo ./front/assets/locales/{locale}/LC_MESSAGES/base")

