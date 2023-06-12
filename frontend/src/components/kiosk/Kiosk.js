import React, { Component } from "react";
//import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
//import { deleteNote, updateNote } from "./NotesActions";
import "./Kiosk.css";
//import { Button } from "react-bootstrap";

class Kiosk extends Component {
    constructor(props) {
        super(props);
        this.state = {
          unit: ""
        };
      }
    render() {
        return (
        <div id='kiosk'>
            <div id='events'>

            </div>

            <div id='signin'>
                <h1>Kiosk</h1>
            </div>

            <div id='users'>
                
            </div>
        </div>
        );
    }
}

Kiosk.propTypes = {};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, {
    
  })(withRouter(Kiosk));