HOMEPAGE_PAGE = """
import { Outlet } from "react-router";
import Sidebar from "../../components/Sidebar/Sidebar";
import { useRef, useState } from "react";
import Navbar from "../../components/Navbar/Navbar";
import useClickOutside from "../../hooks/useClickOutside";

const HomePageLayout = () => {
  const [isSidebarVisible, setIsSidebarVisible] = useState(false);
  const sidebarRef = useRef<HTMLDivElement>(null);

  const toggleSidebar = () => {
    setIsSidebarVisible((prev) => !prev);
  };

  useClickOutside(sidebarRef as React.RefObject<HTMLElement>, () => {
    setIsSidebarVisible(false);
  });

  return (
    <header>
      <div
        ref={sidebarRef}
      >
        <Sidebar
          toggleSidebar={toggleSidebar}
          isCollapsed={!isSidebarVisible}
        />
      </div>
      <main className="pl-10 w-full">
        <Navbar />
        <section className='py-4 px-4 w-full '>
          <Outlet />
        </section>
      </main>
    </header>
  );
};

export default HomePageLayout;
"""

