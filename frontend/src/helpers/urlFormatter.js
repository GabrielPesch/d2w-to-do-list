export const normalizeUrlParams = (queryParams) => {
  if (!queryParams) {
    return "";
  }

  let urlString = "";
  Object.entries(queryParams).forEach(([key, value]) => {
    if (key === "categories_id" && Array.isArray(value)) {
      value.forEach((id) => {
        urlString += `category_id=${encodeURIComponent(id)}&`;
      });
    } else {
      urlString += `${encodeURIComponent(key)}=${encodeURIComponent(value)}&`;
    }
  });

  urlString = urlString.slice(0, -1);
  return urlString;
};
