import { instancedBaseUrl } from "./baseUrl";

const URL_PREFIX = "api/v1/categories";

export const getAllCategories = async () => {
  const URI = `${URL_PREFIX}/`;
  const axiosInstance = instancedBaseUrl();
  const response = await axiosInstance.get(URI);
  if (response.data.success === true) {
    return response.data;
  }
  throw new Error("cant_create_account_error");
};
