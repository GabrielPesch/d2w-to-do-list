import { GithubOutlined, LinkedinOutlined } from "@ant-design/icons";
import { Footer } from "antd/es/layout/layout";
import "./FooterStyle.css";

const AppFooter = () => {
  return (
    <Footer
      style={{
        textAlign: "center",
        backgroundColor: "#F7F7F7",
      }}
    >
      Desenvolvido por Gabriel Pesch ©2024
      <br />
      <a
        href="https://github.com/GabrielPesch?tab=repositories"
        target="_blank"
        rel="noopener noreferrer"
      >
        <GithubOutlined />
      </a>
      <a
        href="https://www.linkedin.com/in/gabrielpesch/"
        target="_blank"
        rel="noopener noreferrer"
      >
        <LinkedinOutlined />
      </a>
    </Footer>
  );
};

export default AppFooter;
