from crawlers.k_c import konga_crawler
from crawlers.j_c import jumia_crawler
import threading
def black_rock():
    # Jumia jumia crawler
    jumia_crawler()

    # Activates konga crawler
    # konga_crawler()
    
    
    # Activates aliexpress crawler
    # alii()

    # Does the yudala magic
    # yudala()

    t = threading.Timer(172800.0, black_rock)
    t.start()
