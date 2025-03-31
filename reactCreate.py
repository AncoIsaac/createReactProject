#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path
import argparse
from templates import TEMPLATES
from style import TEMPLATESCSS

def parse_arg():
    parser = argparse.ArgumentParser(description="Creador de proyectos Vite con React + typeScript")
    parser.add_argument("--name", help="Nombre del proyecto")    
    return parser.parse_args()

def ask_for_project_name():
    """Pregunta el nombre del proyecto si no se proporcionó como argumento."""
    print("\n✨ ¿Cómo quieres llamar a tu proyecto?")
    while True:
        name = input("> Nombre del proyecto (sin espacios ni caracteres especiales): ").strip()
        if name:
            return name
        print("❌ El nombre no puede estar vacío. Intenta de nuevo.")

def chech_requirements():
    print(f"Verificando si nodeJs y npm estan instalados")
    try:
        subprocess.run(["node","--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("❌ Error: Node.js y npm deben estar instalados")
        sys.exit(1)

def create_vite_project(project_name):
    subprocess.run([
        "npm", "create", "vite@latest",
        project_name,
        "--", "--template", "react-swc-ts"
    ],check=True)

    print("📦 Instalando dependencias base...")
    subprocess.run(["npm", "install"], cwd=project_name, check=True)

def install_dependencies(project_name):
    deps = [
        "swr", "axios", "zustand",
        "tailwindcss","@tailwindcss/vite", "react-router", "lucide-react"
    ]
    print("🔧 Instalando dependencias adicionales...")
    subprocess.run(["npm", "install", *deps], cwd=project_name, check=True)


def create_project_structure(project_name):
    print("Creando sidebar, navbar, clickOutSide y homePage ")
    base = Path(project_name) / "src"

    (base / "components/Sidebar/Style").mkdir(parents=True)
    (base / "components/Sidebar/Sidebar.tsx").write_text(TEMPLATES["sidebar"])
    (base / "components/Sidebar/Style/Sidebar.module.css").write_text(TEMPLATESCSS["sidebarStyle"])

    (base / "components/Navbar/Style").mkdir(parents=True)
    (base / "components/Navbar/Navbar.tsx").write_text(TEMPLATES["navbar"])
    (base / "components/Navbar/Style/Navbar.module.css").write_text(TEMPLATESCSS["navbarStyle"])

    (base / "hooks").mkdir()
    (base / "hooks/useClickOutside.ts").write_text(TEMPLATES["clickOutside"])

    (base / "page/home").mkdir(parents=True)
    (base / "page/home/HomePageLayout.tsx").write_text(TEMPLATES["homePage"])
    (base / "page/HomeLayout.tsx").write_text(TEMPLATES["homeLayout"])

    (base / "router").mkdir()
    (base / "router/Router.tsx").write_text(TEMPLATES["router"])

    (base / "App.tsx").write_text(TEMPLATES["app"] )

    (base / "index.css").write_text(TEMPLATESCSS["resetCss"])
    

def main():
    args = parse_arg()

    # Paso 2: Preguntar nombre si no se proporcionó
    project_name = args.name if args.name else ask_for_project_name()

    try:
        chech_requirements()
        
        create_vite_project(project_name)
        install_dependencies(project_name)

        create_project_structure(project_name)

        print(f"\n✅ ¡Proyecto {project_name} creado con éxito!")
        print("\nPara iniciar el desarrollo:")
        print(f"  cd {project_name} && npm run dev")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error durante la creación del proyecto: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    

