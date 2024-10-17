import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  token: null,
  agentId: null,
  email: null,
  voice: null,
  currentAgentName: null,
};

export const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    setToken: (state, action) => {
      state.token = action.payload;
      console.log(state.token,'redux')
    },
    setAgentId: (state, action) => {
      state.agentId = action.payload;
      console.log(state.agentId,'redux')
    },
    setEmail: (state, action) => {
      state.email = action.payload;
      console.log(state.email,'redux')
    },
    setVoice: (state, action) => {
      state.voice = action.payload;
    },
    setCurrentAgentName: (state, action) => {
      state.currentAgentName = action.payload;
    },
  },
});

export const { setToken, setAgentId, setEmail, setVoice, setCurrentAgentName } = chatSlice.actions;

export default chatSlice.reducer;