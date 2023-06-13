import React, { Component } from "react";
//import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
//import { deleteNote, updateNote } from "./NotesActions";
import "./Kiosk.css";
//import { Button } from "react-bootstrap";

class EventList extends Component {
    constructor(props) {
        super(props);
        this.state = {
          unit: ""
        };
      }
    render() {
        return (
          <div id='event_list'>
              <h3>Event List</h3>
          </div>
        );
    }
}

EventList.propTypes = {};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, {
    
  })(withRouter(EventList));