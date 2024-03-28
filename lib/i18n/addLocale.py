import sys
import os

locale = sys.argv[1]
# en

os.system(f"lib/i18n/pygettext.py -d base -o ./front/assets/locales/{locale}/LC_MESSAGES/base.po")

