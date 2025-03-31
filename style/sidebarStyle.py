SIDEBAR_CSS = """
.container {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: 250px;
  background-color: #1e293b;
  transition: width 0.3s ease;
  padding: 5px 6px;
  z-index: 1000;
  overflow: hidden;
}

/* Estado colapsado */
.collapsed {
  width: 40px;
}

.container__div {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 5px;
  border-bottom: 1px solid #c7d0dd;
}
"""




