import {
  Button,
  Flex,
  Form,
  Image,
  Input,
  Layout,
  Typography,
  message,
} from "antd";
import { Content } from "antd/es/layout/layout";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { signUp } from "../../../api/SessionApi";

const SignUpForm = () => {
  const [isFormValid, setIsFormValid] = useState(false);
  const [messageApi, contextHolder] = message.useMessage();
  const [form] = Form.useForm();
  const navigate = useNavigate();

  const onFinish = async (values) => {
    try {
      const response = await signUp({
        email: values.email,
        password: values.password,
        name: values.name,
      });
      localStorage.setItem("access_token", response.data);
      navigate("/home");
    } catch (error) {
      messageApi.open({
        type: "error",
        content:
          "Não foi possível cadastrar seu usuário, tente novamente mais tarde!",
      });
    }
  };

  const handleSignInButton = () => {
    navigate("/");
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
      <>{contextHolder}</>
      <Flex className="flex sign-out">
        <Content className="content">
          <h1 className="title">Cadastrar sua conta</h1>
          <Form
            className="form"
            name="normal_login"
            initialValues={{ remember: true }}
            onFinish={onFinish}
            layout="vertical"
            onFieldsChange={handleFormValidation}
          >
            <Form.Item
              label="Nome"
              name="name"
              rules={[
                { required: true, message: "Por favor, insira seu nome!" },
              ]}
            >
              <Input className="input" placeholder="Nome" />
            </Form.Item>
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
                { required: true, message: "Por favor, insira sua senha!" },
              ]}
            >
              <Input className="input" type="password" placeholder="Senha" />
            </Form.Item>
            <Form.Item
              label="Confirmar Senha"
              name="confirm"
              dependencies={["password"]}
              hasFeedback
              rules={[
                {
                  required: true,
                  message: "Por favor, confirme sua senha!",
                },
                ({ getFieldValue }) => ({
                  validator(_, value) {
                    if (!value || getFieldValue("password") === value) {
                      return Promise.resolve();
                    }
                    return Promise.reject(
                      new Error(
                        "As duas senhas que você inseriu não são iguais!"
                      )
                    );
                  },
                }),
              ]}
            >
              <Input
                className="input"
                type="password"
                placeholder="Confirmar Senha"
              />
            </Form.Item>
            <Form.Item>
              <Button
                className="button"
                type="primary"
                htmlType="submit"
                block
                disabled={!isFormValid}
              >
                Cadastrar
              </Button>
            </Form.Item>
            <Flex className="register-card">
              <Typography style={{ textAlign: "center" }}>
                Já sou cadastrado
              </Typography>
              <Button
                className="button"
                type="primary"
                block
                onClick={handleSignInButton}
              >
                Entrar
              </Button>
            </Flex>
          </Form>
        </Content>
        <Flex className="sider sider-sign-up-img">
          <Image />
        </Flex>
      </Flex>
    </Layout>
  );
};

export default SignUpForm;
