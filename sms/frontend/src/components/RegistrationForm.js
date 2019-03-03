import React from "react";
import { Form } from "semantic-ui-react";

import axios from "axios";

const dosageUnitOptions = [
  { key: "mg", text: "mg", value: "mg" },
  { key: "ml", text: "ml", value: "ml" }
];
const periodUnitOptions = [
  { key: "daily", text: "daily", value: "daily" },
  { key: "weekly", text: "weekly", value: "weekly" },
  { key: "bi-weekly", text: "bi-weekly", value: "bi-weekly" },
  { key: "monthly", text: "monthly", value: "monthly" }
];
class RegistrationForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      first_name: "AIDEN",
      last_name: "LOW",
      phone_number: "8326204829",
      medications: [
        {
          med_name: "advil",
          dosage: "200",
          dosage_unit: "mg",
          frequency: "2",
          time_period: "daily"
        }
      ]
    };
  }

  handleAddClick() {
    this.setState(prevState => ({
      medications: [
        ...prevState.medications,
        {
          med_name: "",
          dosage: "",
          dosage_unit: "mg",
          frequency: "",
          time_period: "daily"
        }
      ]
    }));
  }

  handleChange(index, e) {
    const { name, value } = e.target;
    let medications = [...this.state.medications];
    medications[index] = { ...medications[index], [name]: value };
    this.setState({ medications });
  }

  handleRemoveClick(index) {
    let medications = [...this.state.medications];
    medications.splice(index, 1);
    this.setState({ medications });
  }

  createMedicationFormPortion() {
    return this.state.medications.map((med, index) => (
      <div key={index}>
        <Form.Input
          fluid
          label="Medication"
          value={med.med_name}
          name="med_name"
          onChange={this.handleChange.bind(this, index)}
          placeholder="Medication Name"
          style={{ width: "65%" }}
        />
        <Form.Group widths="equal" style={{ width: "50%" }}>
          <Form.Input
            fluid
            label="Dosage"
            value={med.dosage}
            name="dosage"
            onChange={this.handleChange.bind(this, index)}
            placeholder="Dosage"
          />
          <Form.Select
            fluid
            label="Unit"
            value={med.dosage_unit}
            name="dosage_unit"
            onChange={this.handleChange.bind(this, index)}
            options={dosageUnitOptions}
            placeholder="Unit"
          />
        </Form.Group>
        <Form.Group widths="equal" style={{ width: "50%" }}>
          <Form.Input
            fluid
            label="Frequency"
            value={med.frequency}
            name="frequency"
            onChange={this.handleChange.bind(this, index)}
            placeholder="Frequency"
          />
          <Form.Select
            fluid
            label="Time Period"
            value={med.time_period}
            name="time_period"
            onChange={this.handleChange.bind(this, index)}
            options={periodUnitOptions}
            placeholder="Time Period"
          />
        </Form.Group>
        {index >= 1 && (
          <Form.Button
            className="override"
            value="remove"
            onClick={this.handleRemoveClick.bind(this, index)}
            style={{ backgroundColor: "lightcoral" }}
          >
            Remove
          </Form.Button>
        )}
        <br />
      </div>
    ));
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = e => {
    e.preventDefault();

    const { first_name, last_name, phone_number, medications } = this.state;
    let final_phone_number = phone_number;
    if (phone_number.charAt(0) !== "+") {
      final_phone_number = "+1" + phone_number;
    }
    console.log("calling axios", first_name, last_name);
    axios
      .post("http://localhost:80/api/register_user", {
        first_name,
        last_name,
        medications,
        phone_number: final_phone_number
      })
      .then(result => {
        alert(result.data.token);
      });
  };

  render() {
    const { first_name, last_name, phone_number } = this.state;

    return (
      <Form style={{ padding: "35px" }}>
        <h2 className="ui horizontal divider header">
          <i className="fas fa-user-alt" style={{ paddingRight: "5px" }} />
          Patient Information
        </h2>
        <Form.Group widths="equal">
          <Form.Input
            fluid
            label="First Name"
            name="first_name"
            value={first_name}
            onChange={this.onChange}
            placeholder="First name"
          />
          <Form.Input
            fluid
            label="Last Name"
            name="last_name"
            value={last_name}
            onChange={this.onChange}
            placeholder="Last name"
          />
        </Form.Group>
        <Form.Input
          fluid
          label="Phone Number"
          name="phone_number"
          value={phone_number}
          onChange={this.onChange}
          placeholder="Phone Number"
          style={{ width: "40%" }}
        />
        <h2 className="ui horizontal divider header">
          <i className="fas fa-pills" style={{ paddingRight: "5px" }} />
          Prescriptions
        </h2>
        {this.createMedicationFormPortion()}
        <br />
        <hr />
        <Form.Button value="Add More" onClick={this.handleAddClick.bind(this)}>
          Add More
        </Form.Button>
        <Form.Button
          onClick={this.handleSubmit}
          style={{ backgroundColor: "mediumseagreen" }}
        >
          Submit
        </Form.Button>
      </Form>
    );
  }
}

export default RegistrationForm;
