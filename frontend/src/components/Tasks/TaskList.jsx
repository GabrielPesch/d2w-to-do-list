import React, { useEffect, useMemo, useState } from "react";
import {
  List,
  Typography,
  Collapse,
  Button,
  Pagination,
  Skeleton,
  Tooltip,
  Flex,
} from "antd";
import {
  EditOutlined,
  DeleteOutlined,
  CheckOutlined,
  CloseOutlined,
} from "@ant-design/icons";
import TaskForm from "../Forms/TaskForm/TaskForm";
import { useDispatch, useSelector } from "react-redux";
import {
  deleteTaskThunk,
  finishTaskThunk,
  loadTasksThunk,
} from "../../actions/tasksSlice";
import "./TaskListStyles.css";

const { Text } = Typography;
const { Panel } = Collapse;

const TaskList = () => {
  const [arrow] = useState("Show");
  const dispatch = useDispatch();
  const tasks = useSelector((state) => state.task.items);
  const isLoaded = useSelector((state) => state.task.isLoaded);
  const pagination = useSelector((state) => state.task.pagination);
  const [expandedKeys, setExpandedKeys] = useState([]);
  const [isEditing, setIsEditing] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const selectedCategories = useSelector(
    (state) => state.category.selectedCategories
  );
  const [queryParams, setQueryParams] = useState({
    page: 1,
    per_page: 10,
    categories_id: selectedCategories,
  });

  useEffect(() => {
    dispatch(
      loadTasksThunk({ ...queryParams, categories_id: selectedCategories })
    );
  }, [dispatch, selectedCategories, queryParams]);

  const handlePageChange = (page, pageSize) => {
    setQueryParams((prevParams) => ({
      ...prevParams,
      categories_id: selectedCategories,
      page,
      per_page: pageSize,
    }));
  };

  const toggleCompleted = (id) => {
    dispatch(finishTaskThunk(id));
  };

  const editTask = (id) => {
    const taskToEdit = tasks.find((task) => task.id === id);
    setEditingTask(taskToEdit);
    setIsEditing(true);
  };

  const handleCancel = () => {
    setIsEditing(false);
    setEditingTask(null);
  };

  const deleteTask = (id) => {
    dispatch(deleteTaskThunk(id));
  };

  const handleExpand = (taskId) => {
    const currentIndex = expandedKeys.indexOf(taskId);
    const newExpandedKeys = [...expandedKeys];

    if (currentIndex === -1) {
      newExpandedKeys.push(taskId);
    } else {
      newExpandedKeys.splice(currentIndex, 1);
    }

    setExpandedKeys(newExpandedKeys);
  };

  const mergedArrow = useMemo(() => {
    if (arrow === "Hide") {
      return false;
    }

    if (arrow === "Show") {
      return true;
    }

    return {
      pointAtCenter: true,
    };
  }, [arrow]);

  return (
    <>
      {!isLoaded && (
        <>
          <Skeleton active />
          <Skeleton active />
          <Skeleton active />
          <Skeleton active />
          <Skeleton active />
          <Skeleton active />
        </>
      )}

      {isLoaded && (
        <List
          className="task-list-list"
          itemLayout="horizontal"
          dataSource={tasks}
          renderItem={(task) => (
            <List.Item
              actions={[
                <Flex className="task-list-item">
                  <Tooltip
                    placement="topLeft"
                    title={"Concluir tarefa"}
                    arrow={mergedArrow}
                  >
                    <Button
                      className="task-list-button"
                      icon={<CheckOutlined />}
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleCompleted(task.id);
                      }}
                    />
                  </Tooltip>
                  <Tooltip
                    placement="topLeft"
                    title={"Editar tarefa"}
                    arrow={mergedArrow}
                  >
                    <Button
                      className="task-list-button"
                      icon={<EditOutlined />}
                      onClick={(e) => {
                        e.stopPropagation();
                        editTask(task.id);
                      }}
                    />
                  </Tooltip>
                  <Tooltip
                    placement="topLeft"
                    title={"Excluir tarefa"}
                    arrow={mergedArrow}
                  >
                    <Button
                      className="task-list-button"
                      danger
                      icon={<DeleteOutlined />}
                      onClick={(e) => {
                        e.stopPropagation();
                        deleteTask(task.id);
                      }}
                    />
                  </Tooltip>
                </Flex>,
              ]}
              onClick={() => handleExpand(task.id)}
              style={{ cursor: "pointer" }}
            >
              <List.Item.Meta
                title={
                  <Text
                    strong
                    type={task.completed ? "warning" : "success"}
                    delete={task.completed}
                    className="task-list-title"
                  >
                    {task.completed ? (
                      <CheckOutlined
                        className="task-list-title-icon"
                        twoToneColor={task.completed ? "warning" : "success"}
                      />
                    ) : (
                      <CloseOutlined className="task-list-title-icon" />
                    )}
                    {task.title}
                  </Text>
                }
                description={
                  <Collapse
                    activeKey={expandedKeys.includes(task.id) ? [task.id] : []}
                    bordered={false}
                  >
                    <Panel header={false} key={task.id} showArrow={true}>
                      <p>{task.description}</p>
                    </Panel>
                  </Collapse>
                }
              />
            </List.Item>
          )}
        />
      )}
      {isEditing && (
        <TaskForm
          isEditing={isEditing}
          isModalVisible={isEditing}
          taskValues={editingTask}
          onCancel={handleCancel}
        />
      )}
      {pagination.totalPages > 1 && (
        <Flex className="task-list-pagination-flex">
          <Pagination
            className="task-list-pagination"
            current={pagination.currentPage}
            onChange={handlePageChange}
            total={pagination.totalPages * pagination.perPage}
            totalPages={pagination.totalPages}
            pageSize={pagination.perPage}
            showSizeChanger={false}
          />
        </Flex>
      )}
    </>
  );
};

export default TaskList;
