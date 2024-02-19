import React, { useEffect, useState } from "react";
import { Button, Drawer, Layout, Menu, Skeleton } from "antd";
import "./SidebarStyles.css";
import { useDispatch, useSelector } from "react-redux";
import { loadCategoriesThunk } from "../../actions/categoriesSlice";
import {
  addSelectedCategory,
  removeSelectedCategory,
} from "../../actions/categoriesSlice";
import { PlusOutlined } from "@ant-design/icons";

const { Sider } = Layout;

const AppSideBar = () => {
  const dispatch = useDispatch();
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768);
  const [visible, setVisible] = useState(false);
  const {
    isLoaded,
    data: categories,
    selectedCategories,
  } = useSelector((state) => state.category);

  useEffect(() => {
    dispatch(loadCategoriesThunk());

    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
    };

    window.addEventListener("resize", handleResize);

    return () => window.removeEventListener("resize", handleResize);
  }, [dispatch]);

  const toggleCategorySelection = (categoryId) => {
    if (selectedCategories.includes(categoryId)) {
      dispatch(removeSelectedCategory(categoryId));
    } else {
      dispatch(addSelectedCategory(categoryId));
    }
  };

  const toggleDrawer = () => {
    setVisible(!visible);
  };

  const sidebarContent = (
    <>
      {!isLoaded ? (
        <>
          <Skeleton active />
          <Skeleton active />
        </>
      ) : (
        <Menu
          mode="inline"
          multiple={true}
          onClick={({ key }) => toggleCategorySelection(key)}
          selectedKeys={selectedCategories}
        >
          {categories.map((category) => (
            <Menu.Item key={category.id}>{category.name}</Menu.Item>
          ))}
        </Menu>
      )}
    </>
  );

  return (
    <>
      {isMobile ? (
        <>
          <Drawer
            title="Categories"
            placement="left"
            closable={false}
            onClose={toggleDrawer}
            visible={visible}
            className="drawer-categories"
          >
            {sidebarContent}
          </Drawer>
          <br />
          <Button
            className="drawer-button"
            type="primary"
            onClick={toggleDrawer}
            icon={<PlusOutlined />}
          >
            Ver categorias
          </Button>
        </>
      ) : (
        <Sider className="sidebar-content">{sidebarContent}</Sider>
      )}
    </>
  );
};

export default AppSideBar;
