import React from "react";
import { Form } from "semantic-ui-react";

const options = [
  { key: "mg", text: "mg", value: "mg" },
  { key: "ml", text: "ml", value: "ml" }
];
class RegistrationForm extends React.Component {
  state = {};

  handleChange = (e, { value }) => this.setState({ value });

  render() {
    const { value } = this.state;
    return (
      <Form>
        <h2 class="ui dividing header">Patient Information</h2>
        <Form.Group widths="equal">
          <Form.Input fluid label="First Name" placeholder="First name" />
          <Form.Input fluid label="Last Name" placeholder="Last name" />
        </Form.Group>
        <Form.Input
          fluid
          label="Phone Number"
          placeholder="Phone Number"
          style={{ width: "40%" }}
        />
        <h2 class="ui dividing header">Prescriptions</h2>
        <Form.Input
          fluid
          label="Medication Name"
          placeholder="Medication Name"
          style={{ width: "65%" }}
        />
      </Form>
    );
  }
}

export default RegistrationForm;
