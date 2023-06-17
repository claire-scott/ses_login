import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
//import { deleteNote, updateNote } from "./NotesActions";
import "./Kiosk.css";
import EventsList from "./EventsList";
//import { Button } from "react-bootstrap";

import { logout } from "../login/LoginActions";
import CheckoutList from "./CheckoutList";

class Kiosk extends Component {
    constructor(props) {
        super(props);
        this.state = {
          unit: ""
        };
      }
    render() {
        const { user } = this.props.auth;
        return (
          <div id='body'>
            <div id='bs_body' class="container-fluid h-100 d-flex flex-column">
                <nav class="navbar navbar-expand-sm  navbar-dark bg-primary">
                    <div>
                    <a class="brand navbar-brand" href="/">SES</a>
                    </div>
                    <div class="collapse navbar-collapse"></div>
                    <div class="d-flex justify-content-end">
                  <span class="navbar-text">
                    User: <b>{user.username}</b>
                  </span>
                  <a href='#' onClick={this.onLogout}>Logout</a>
                  </div>
                </nav>

              <div id='kiosk' class="row flex-fill">

                  <div id='events' class='col'>
                    <EventsList />
                  </div>

                  <div id='signin' class='col-6'>
                      <h1>Kiosk</h1>
                  </div>

                  <div id='users'class='col'>
                      <CheckoutList />
                  </div>

            </div>
            </div>
          </div>
        );
    }
}


Kiosk.propTypes = {
  logout: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps, {
    logout
  })(withRouter(Kiosk));