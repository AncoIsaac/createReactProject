HOMEPAGE_LAYOUT_TSX = """import { Outlet } from "react-router-dom";
import Sidebar from "../../components/Sidebar/Sidebar";
import Navbar from "../../components/Navbar/Navbar";
import { useRef, useState } from "react";
import { useClickOutside } from "../../hooks/useClickOutside";

const HomePageLayout = () => {
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
  const sidebarRef = useRef<HTMLDivElement>(null);

  useClickOutside(sidebarRef, () => {
    if (!isSidebarCollapsed) {
      setIsSidebarCollapsed(true);
    }
  });

  return (
    <div className="flex h-screen bg-gray-100">
      <div ref={sidebarRef}>
        <Sidebar
          toggleSidebar={() => setIsSidebarCollapsed(!isSidebarCollapsed)}
          isCollapsed={isSidebarCollapsed}
        />
      </div>
      <div className="flex-1 flex flex-col overflow-hidden">
        <Navbar />
        <main className="flex-1 overflow-y-auto p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default HomePageLayout;
"""

