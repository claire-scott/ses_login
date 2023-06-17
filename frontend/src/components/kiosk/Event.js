import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { deleteEvent, updateEvent } from "./EventsActions";
import { Button } from "react-bootstrap";

class Event extends Component {

  render() {
    const { event } = this.props;
    return (
      <div>
        <hr />
        <p>
            (id:{event.id}) {event.description}
        </p>
        <p>
            {event.event_type.event_category} - {event.event_type.event_type}
        </p>
        <p>
            {event.event_type.active_from} - {event.event_type.active_to}
        </p>
        
      </div>
    );
  }
}

Event.propTypes = {
  event: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});

export default connect(mapStateToProps, { deleteEvent, updateEvent })(
  withRouter(Event)
);
