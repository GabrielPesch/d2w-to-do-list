import React from "react";
import { Route, Routes } from "react-router-dom";
import SignIn from "../pages/sign_in";
import SignUp from "../pages/sign_up";
import Home from "../pages/home";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<SignIn />} />
      <Route path="/signup" element={<SignUp />} />
      <Route path="/home" element={<Home />} />
    </Routes>
  );
};

export default AppRoutes;
