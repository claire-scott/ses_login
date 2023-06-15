import React, { Component } from "react";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import "./Kiosk.css";

class CheckoutList extends Component {
    constructor(props) {
        super(props);
        this.state = {
          unit: ""
        };
      }
    render() {
        return (
          <div id='checkout_list'>
              <h3>Checkout List</h3>
          </div>
        );
    }
}

CheckoutList.propTypes = {};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, {
    
  })(withRouter(CheckoutList));