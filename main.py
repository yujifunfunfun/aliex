import eel
from fetch_aliex import *


@eel.expose
def fetch_aliex(category,keyword,delete_keyword,min_price,max_price,free_delivery,evaluation,min_sales_figures,max_sales_figures):
    main(category,keyword,delete_keyword,min_price,max_price,free_delivery,evaluation,min_sales_figures,max_sales_figures)

eel.init("web")
eel.start("main.html",size=(600, 800))