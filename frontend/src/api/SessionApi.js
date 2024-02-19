import baseUrl from "./baseUrl";

const URL_PREFIX = "api/v1/session";

export const signIn = async ({ email, password }) => {
  const URI = `${URL_PREFIX}/sign_in`;

  const response = await baseUrl.post(URI, {
    email,
    password,
  });

  if (response.data.success === true) {
    return response.data;
  }
  throw new Error("invalid_credentials");
};

export const signUp = async ({ email, password, name }) => {
  const URI = `${URL_PREFIX}/sign_up`;

  const response = await baseUrl.post(URI, {
    email,
    password,
    name,
  });

  if (response.data.success === true) {
    return response.data;
  }
  throw new Error("sign_up_error");
};

export const signOut = async () => {
  const URI = `${URL_PREFIX}/sign_out`;
  localStorage.removeItem("access_token");

  try {
    localStorage.removeItem("access_token");
    const response = await baseUrl.post(URI);
    if (response.data.success === true) {
      return response.data;
    }
    // toast
  } catch (error) {
    console.log(error);
    // toast
  }
};
