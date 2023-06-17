import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { getEvents } from "./EventsActions";

import Event from "./Event";

class EventsList extends Component {
  componentDidMount() {
    this.props.getEvents();
  }

  render() {
    const { events } = this.props;

    if (events.length === 0) {
      return <h2>No current events</h2>;
    }

    let items = events.map(event => {
      return <Event key={event.id} event={event} />;
    });

    return (
      <div>
        <h2>Events</h2>
        {items}
        <hr /> {/* a */}
      </div>
    );
  }
}

EventsList.propTypes = {
  getEvents: PropTypes.func.isRequired,
  events: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  events: state.events
});

export default connect(mapStateToProps, {
  getEvents
})(withRouter(EventsList));
