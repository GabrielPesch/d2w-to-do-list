import React, { useEffect, useState } from "react";
import { Header } from "antd/es/layout/layout";
import { Button, Image } from "antd";
import { PlusOutlined, LogoutOutlined } from "@ant-design/icons";
import { useNavigate } from "react-router-dom";
import { signOut } from "../../api/SessionApi";
import TaskForm from "../Forms/TaskForm/TaskForm";
import d2wlogo from "../../images/d2wlogo.webp";
import "./AppHeaderStyle.css";

const AppHeader = () => {
  const [isModalVisible, setIsModalVisible] = useState(false);
  const navigate = useNavigate();
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
    };

    window.addEventListener("resize", handleResize);

    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const showModal = () => {
    setIsModalVisible(true);
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  const handleLogout = async () => {
    await signOut();
    navigate("/");
  };

  return (
    <Header className={"app-header"}>
      {!isMobile && (
        <Image
          src={d2wlogo}
          alt="Logo"
          width={120}
          className="header-icon"
          preview={false}
        />
      )}

      <div className="shouldNotShow">
        <Button icon={<PlusOutlined />} onClick={showModal}>
          Adicionar Tarefa
        </Button>
        <Button
          icon={<LogoutOutlined />}
          style={{ marginLeft: "10px" }}
          onClick={handleLogout}
        >
          Sair
        </Button>
      </div>
      {isModalVisible && (
        <TaskForm isModalVisible={isModalVisible} onCancel={handleCancel} />
      )}
    </Header>
  );
};

export default AppHeader;
