import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Form, Input, Button, Select, Modal } from "antd";
import { loadCategoriesThunk } from "../../../actions/categoriesSlice";
import { createTaskThunk, updateTaskThunk } from "../../../actions/tasksSlice";

const TaskForm = ({ isEditing, taskValues, onCancel, isModalVisible }) => {
  const dispatch = useDispatch();
  const { isLoading, data: categories } = useSelector(
    (state) => state.category
  );
  const [form] = Form.useForm();

  useEffect(() => {
    dispatch(loadCategoriesThunk());
    if (isEditing && taskValues) {
      form.setFieldsValue({
        title: taskValues.title,
        description: taskValues.description,
        category_id: taskValues.category_id,
      });
    } else {
      form.resetFields();
    }
  }, [dispatch, form, isEditing, taskValues]);

  const onFinish = (values) => {
    if (isEditing) {
      dispatch(updateTaskThunk({ ...values, task_id: taskValues.id }));
    } else {
      dispatch(createTaskThunk(values));
    }
    onCancel();
  };

  return (
    <Modal
      title={isEditing ? "Editar tarefa" : "Adicionar Tarefa"}
      open={isModalVisible}
      onCancel={onCancel}
      footer={null}
    >
      <Form
        form={form}
        name="task_form"
        onFinish={onFinish}
        autoComplete="off"
        layout="vertical"
      >
        <Form.Item
          label="Título"
          name="title"
          rules={[
            { required: true, message: "Por favor, insira o título!" },
            { min: 3, message: "O título deve ter no mínimo 3 caracteres!" },
            {
              max: 50,
              message: "O título deve ter no máximo 50 caracteres!",
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          label="Descrição"
          name="description"
          rules={[
            {
              max: 500,
              message: "A descrição deve ter no máximo 500 caracteres!",
            },
          ]}
        >
          <Input.TextArea />
        </Form.Item>
        <Form.Item
          label="Categoria"
          name="category_id"
          rules={[
            { required: true, message: "Por favor, selecione uma categoria!" },
          ]}
        >
          <Select loading={isLoading} placeholder="Selecione uma categoria">
            {categories.map((category) => (
              <Select.Option key={category.id} value={category.id}>
                {category.name}
              </Select.Option>
            ))}
          </Select>
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            {isEditing ? "Editar tarefa" : "Adicionar Tarefa"}
          </Button>
        </Form.Item>
      </Form>
    </Modal>
  );
};

export default TaskForm;
