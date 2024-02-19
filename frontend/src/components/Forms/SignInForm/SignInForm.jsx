import React, { useState } from "react";
import {
  Form,
  Input,
  Button,
  Layout,
  Typography,
  Flex,
  Image,
  message,
} from "antd";
import "./SignInFormStyles.css";
import { signIn } from "../../../api/SessionApi";
import { useNavigate } from "react-router-dom";
const { Content } = Layout;

const SignInForm = () => {
  const [isFormValid, setIsFormValid] = useState(false);
  const [form] = Form.useForm();
  const navigate = useNavigate();
  const [messageApi, contextHolder] = message.useMessage();

  const onFinish = async (values) => {
    try {
      const response = await signIn({
        email: values.email,
        password: values.password,
      });
      localStorage.setItem("access_token", response.data);

      navigate("/home");
    } catch (error) {
      messageApi.open({
        type: "error",
        content: "Email ou Senha incorretos",
      });
    }
  };

  const handleRegisterButton = () => {
    navigate("/signup");
  };

  const handleFormValidation = () => {
    form
      .validateFields()
      .then(() => {
        setIsFormValid(true);
      })
      .catch((_error) => {
        setIsFormValid(false);
      });
  };

  return (
    <Layout className="layout">
      {contextHolder}
      <Flex className="flex">
        <Content className="content">
          <h1 className="title">Fazer login</h1>
          <Form
            className="form"
            name="normal_login"
            initialValues={{ remember: true }}
            onFinish={onFinish}
            layout="vertical"
            onFieldsChange={handleFormValidation}
          >
            <Form.Item
              label="Email"
              name="email"
              rules={[
                {
                  required: true,
                  message: "Por favor, insira seu Email!",
                },
                {
                  type: "email",
                  message: "O e-mail inserido não é válido!",
                },
              ]}
            >
              <Input className="input" placeholder="Email" />
            </Form.Item>
            <Form.Item
              label="Senha"
              name="password"
              rules={[
                { required: true, message: "Please input your Password!" },
              ]}
            >
              <Input className="input" type="password" placeholder="Password" />
            </Form.Item>
            <Form.Item>
              <Button
                className="button"
                type="primary"
                htmlType="submit"
                block
                disabled={!isFormValid}
              >
                Entrar
              </Button>
            </Form.Item>
            <Flex className="register-card">
              <Typography style={{ textAlign: "center" }}>
                Não tem uma conta?
              </Typography>
              <Button
                className="button"
                type="primary"
                htmlType="submit"
                block
                onClick={handleRegisterButton}
              >
                Cadastre-se
              </Button>
            </Flex>
          </Form>
        </Content>
        <Flex className="sider sider-sign-in-img">
          <Image />
        </Flex>
      </Flex>
    </Layout>
  );
};

export default SignInForm;
