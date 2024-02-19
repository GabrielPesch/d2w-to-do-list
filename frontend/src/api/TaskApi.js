import { normalizeUrlParams } from "../helpers/urlFormatter";
import baseUrl, { instancedBaseUrl } from "./baseUrl";

const URL_PREFIX = "api/v1/tasks";

export const getAllTasks = async (queryParams = {}) => {
  const queryString = normalizeUrlParams(queryParams);
  const URI = `${URL_PREFIX}/?${queryString}`;

  try {
    const axiosInstance = instancedBaseUrl();
    const response = await axiosInstance.get(URI);
    return response.data;
  } catch (error) {
    console.log(error);
  }
};

export const createTask = async ({ title, description, category_id }) => {
  const URI = `${URL_PREFIX}/`;

  try {
    const token = localStorage.getItem("access_token");
    const axiosInstance = instancedBaseUrl(token);
    const response = await axiosInstance.get(URI, {
      title,
      description,
      category_id,
    });

    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const updateTask = async ({
  title,
  description,
  category_id,
  task_id,
}) => {
  const URI = `${URL_PREFIX}/${task_id}`;

  try {
    const response = await baseUrl.put(URI, {
      title,
      description,
      category_id,
    });

    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const finishTask = async (task_id) => {
  const URI = `${URL_PREFIX}/${task_id}`;

  try {
    const response = await baseUrl.patch(URI);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const deleteTask = async (task_id) => {
  const URI = `${URL_PREFIX}/${task_id}`;

  try {
    const response = await baseUrl.delete(URI);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
