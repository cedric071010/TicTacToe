import sys
import os

args = sys.argv
# example.py en

os.system(f"/Library/Frameworks/Python.framework/Versions/3.10/share/doc/python3.10/examples/Tools/i18n/pygettext.py "
          f"-d base -o ./front/assets/locales/{args[1]}/LC_MESSAGES/base.po {args[0]}")

