import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import {
  createTask,
  deleteTask,
  finishTask,
  getAllTasks,
  updateTask,
} from "../api/TaskApi";

export const loadTasksThunk = createAsyncThunk(
  "tasks/loadTasks",
  async (queryParams) => {
    const payload = await getAllTasks({ ...queryParams });
    const response = {
      data: payload.data,
      pagination: payload.pagination,
    };

    return response;
  }
);

export const createTaskThunk = createAsyncThunk(
  "tasks/createTask",
  async (taskData) => {
    const response = await createTask(taskData);
    return response?.data || null;
  }
);

export const updateTaskThunk = createAsyncThunk(
  "tasks/updateTask",
  async (taskData) => {
    const response = await updateTask(taskData);
    return response?.data || null;
  }
);

export const finishTaskThunk = createAsyncThunk(
  "tasks/finishTaskThunk",
  async (task_id) => {
    const payload = await finishTask(task_id);
    const response = {
      success: payload?.success || false,
      data: task_id,
    };
    return response;
  }
);
export const deleteTaskThunk = createAsyncThunk(
  "tasks/deleteTask",
  async (task_id, { dispatch }) => {
    const response = await deleteTask(task_id);
    if (response.success) {
      dispatch(loadTasksThunk());
    }
  }
);

export const tasksSlice = createSlice({
  name: "task",
  initialState: {
    isLoaded: false,
    items: [],
    pagination: {
      perPage: 10,
      currentPage: 1,
      totalPages: 1,
    },
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(loadTasksThunk.pending, (state) => {
        state.isLoaded = false;
        state.items = [];
      })
      .addCase(loadTasksThunk.fulfilled, (state, action) => {
        state.isLoaded = true;
        state.items = action.payload.data;
        state.pagination.currentPage = action.payload.pagination.current_page;
        state.pagination.perPage = action.payload.pagination.per_page;
        state.pagination.totalPages = action.payload.pagination.total_pages;
      })
      .addCase(loadTasksThunk.rejected, (state) => {
        state.isLoaded = false;
        state.items = [];
      })
      .addCase(createTaskThunk.fulfilled, (state, action) => {
        if (action.payload) {
          if (state.items.length >= state.pagination.perPage) {
            state.items.pop();
          }
          state.items.unshift(action.payload);
          state.pagination.totalPages += 1;
        }
      })
      .addCase(updateTaskThunk.fulfilled, (state, action) => {
        if (action.payload) {
          const index = state.items.findIndex(
            (item) => item.id === action.payload.id
          );
          if (index !== -1) {
            state.items[index] = action.payload;
          }
        }
      })
      .addCase(finishTaskThunk.fulfilled, (state, action) => {
        if (action.payload.success) {
          const index = state.items.findIndex(
            (item) => item.id === action.payload.data
          );
          if (index !== -1) {
            state.items[index].completed = !state.items[index].completed;
          }
        }
      });
  },
});

export default tasksSlice.reducer;
