from pyfiglet import Figlet
from time import strftime, localtime
import locale
import sys

def date(format_ = "%Y %d %b, %A", font = "graceful"):
    locale.setlocale(locale.LC_ALL, "")
    fig = Figlet(font = font)
    print(fig.renderText(strftime(format_, localtime())))

date(*sys.argv[1:])
