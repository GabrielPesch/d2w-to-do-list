import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { getAllCategories } from "../api/CategoryApi";

export const loadCategoriesThunk = createAsyncThunk(
  "category/loadCategories",
  async (queryParams) => {
    const response = await getAllCategories({ queryParams });
    return { data: response?.data || [] };
  }
);

export const categoriesSlice = createSlice({
  name: "category",
  initialState: {
    isLoaded: false,
    data: [],
    selectedCategories: [],
  },
  reducers: {
    addSelectedCategory: (state, action) => {
      const category = action.payload;
      if (!state.selectedCategories.includes(category)) {
        state.selectedCategories.push(category);
      }
    },
    removeSelectedCategory: (state, action) => {
      const category = action.payload;
      state.selectedCategories = state.selectedCategories.filter(
        (cat) => cat !== category
      );
    },
  },

  extraReducers: (builder) => {
    builder
      .addCase(loadCategoriesThunk.pending, (state) => {
        state.isLoaded = false;
        state.data = [];
      })
      .addCase(loadCategoriesThunk.fulfilled, (state, action) => {
        state.isLoaded = true;
        state.data = action.payload.data;
      })
      .addCase(loadCategoriesThunk.rejected, (state) => {
        state.isLoaded = false;
        state.data = [];
      });
  },
});

export default categoriesSlice.reducer;
export const { addSelectedCategory, removeSelectedCategory } =
  categoriesSlice.actions;
