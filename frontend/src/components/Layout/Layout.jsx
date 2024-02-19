import { Layout } from "antd";
import AppFooter from "../Footer/Footer";
import AppHeader from "../Header/AppHeader";
import AppSideBar from "../SideBar/Sidebar";
import { layoutStyle } from "./LayoutStyle";

const AppLayout = ({ children }) => {
  return (
    <Layout style={layoutStyle}>
      <AppHeader />
      <Layout>
        <AppSideBar />
        <Layout.Content style={{ padding: "0 24px", minHeight: "280px" }}>
          {children}
        </Layout.Content>
      </Layout>
      <AppFooter />
    </Layout>
  );
};

export default AppLayout;
