from typing import Dict
from .sidebar import SIDEBAR_TSX
from .navbar import NAVBAR_TSX
from .clickOutSide import USE_CLICK_OUTSIDE_TS
from .homePage import HOMEPAGE_LAYOUT_TSX

TEMPLATES: Dict[str, str,] = {
    "sidebar": SIDEBAR_TSX,
    "navbar": NAVBAR_TSX,
    "homePage": HOMEPAGE_LAYOUT_TSX,
    "clickOutSide": USE_CLICK_OUTSIDE_TS
    # Agrega más plantillas aquí según importes más archivos
}
