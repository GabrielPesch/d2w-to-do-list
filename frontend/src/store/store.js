import { configureStore } from "@reduxjs/toolkit";
import categoryReducer from "../actions/categoriesSlice";
import taskReducer from "../actions/tasksSlice";

export const store = configureStore({
  reducer: {
    category: categoryReducer,
    task: taskReducer,
  },
});
