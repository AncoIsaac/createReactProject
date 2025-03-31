from typing import Dict
from .sidebar import SIDEBAR_TSX
from .navbar import NAVBAR_TSX
from .clickOutside import USE_CLICK_OUTSIDE_TS
from .homePage import HOMEPAGE_PAGE
from .homeLayout import HOME_LAYOUT
from .router import ROUTER_TSX
from .app import APP_TSX

TEMPLATES: Dict[str, str,] = {
    "sidebar": SIDEBAR_TSX,
    "navbar": NAVBAR_TSX,
    "homePage": HOMEPAGE_PAGE,
    "clickOutside": USE_CLICK_OUTSIDE_TS,
    "homeLayout": HOME_LAYOUT,
    "router": ROUTER_TSX,
    "app": APP_TSX
    # Agrega más plantillas aquí según importes más archivos
}
