from typing import Dict
from .sidebarStyle import SIDEBAR_CSS
from .navbarStyle import NAVBAR_CSS
from .resetCss import RESET_CSS

TEMPLATESCSS: Dict[str, str]= {
    "sidebarStyle": SIDEBAR_CSS,
    "navbarStyle": NAVBAR_CSS,
    "resetCss": RESET_CSS
    # Agrega más plantillas aquí según importes más archivos
}

