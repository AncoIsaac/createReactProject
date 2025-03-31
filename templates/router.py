ROUTER_TSX = """
import { createBrowserRouter, RouterProvider } from "react-router"
import HomeLayout from "../page/HomeLayout"
import HomePageLayout from "../page/Home/HomePageLayout"
const routerDom = createBrowserRouter([
  {
    path: "/",
    element: <HomeLayout />,
    errorElement: <div>Error</div>,
    children: [
      {
        index: true,
        //puede ser el login o el home
        element: <div>pagina principal</div>,
      },
      {
        path: 'home',
        element: <HomePageLayout/>,
        children: [
          {
            index: true,
            element: <div>example</div>,
          },
          {
            path: 'chess',
            element: <div>example</div>,
          }
        ]
      }
    ]
  }, 
])

const Router = () => {
  return (
    <RouterProvider router={routerDom} />
  )
}

export default Router
"""
