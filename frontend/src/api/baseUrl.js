import axios from "axios";
const accessToken = localStorage.getItem("access_token");

const baseUrl = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${accessToken}`,
  },
});

export const instancedBaseUrl = () => {
  const token = localStorage.getItem("access_token");

  return axios.create({
    baseURL: "http://127.0.0.1:5000/",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });
};

export default baseUrl;
