import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_EVENTS, ADD_EVENT, DELETE_EVENT, UPDATE_EVENT } from "./EventsTypes";

export const getEvents = () => dispatch => {
  axios
    .get("/api/v1/events/")
    .then(response => {
      dispatch({
        type: GET_EVENTS,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const addEvent = event => dispatch => {
  axios
    .post("/api/v1/events/", event)
    .then(response => {
      dispatch({
        type: ADD_EVENT,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const deleteEvent = id => dispatch => {
  axios
    .delete(`/api/v1/events/${id}/`)
    .then(response => {
      dispatch({
        type: DELETE_EVENT,
        payload: id
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};

export const updateEvent = (id, event) => dispatch => {
  axios
    .patch(`/api/v1/events/${id}/`, event)
    .then(response => {
      dispatch({
        type: UPDATE_EVENT,
        payload: response.data
      });
    })
    .catch(error => {
      toastOnError(error);
    });
};
