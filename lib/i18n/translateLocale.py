import sys
import os

locale = sys.argv[1]
# en

os.system(f"lib/i18n/msgfmt.py -o ./front/assets/locales/{locale}/LC_MESSAGES/base.mo "
          f"./front/assets/locales/{locale}/LC_MESSAGES/base")
