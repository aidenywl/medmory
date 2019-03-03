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
      first_name: "Fiona",
      last_name: "Tang",
      phone_number: "+14159198310",
      medication0: {
        med_name: "advil",
        dosage: "200",
        dosage_unit: "mg",
        frequency: "2",
        time_period: "weekly"
      },
      medication1: {
        med_name: "paracetamol",
        dosage: "500",
        dosageUnit: "ml",
        frequency: "1",
        time_period: "daily"
      },
      medication2: {
        med_name: "Acetaminophen",
        dosage: "500",
        dosageUnit: "mg",
        frequency: "2",
        time_period: "bi-weekly"
      }
    };
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onMedication0Change = e => {
    this.setState({
      medication0: {
        [e.target.name]: e.target.value
      }
    });
  };

  onMedication1Change = e => {
    this.setState({
      medication1: {
        [e.target.name]: e.target.value
      }
    });
  };

  onMedication2Change = e => {
    this.setState({
      medication2: {
        [e.target.name]: e.target.value
      }
    });
  };

  handleSubmit = e => {
    e.preventDefault();

    const {
      first_name,
      last_name,
      phone_number,
      medication0,
      medication1,
      medication2
    } = this.state;
    console.log("calling axios");
    axios
      .post("/api/register_user", {
        first_name,
        last_name,
        phone_number,
        medication0,
        medication1,
        medication2
      })
      .then(result => {
        alert(result.data.token);
      });
  };

  render() {
    const {
      first_name,
      last_name,
      phone_number,
      medication0,
      medication1,
      medication2
    } = this.state;

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
        <Form.Input
          fluid
          label="Medication 1"
          value={medication0.med_name}
          name="med_name"
          onChange={this.onMedication0Change}
          placeholder="Medication Name"
          style={{ width: "65%" }}
        />
        <Form.Group widths="equal" style={{ width: "50%" }}>
          <Form.Input
            fluid
            label="Dosage"
            value={medication0.dosage}
            name="dosage"
            onChange={this.onMedication0Change}
            placeholder="Dosage"
          />
          <Form.Select
            fluid
            label="Unit"
            value={medication0.dosageUnit}
            name="dosage_unit"
            onChange={this.onMedication0Change}
            options={dosageUnitOptions}
            placeholder="Unit"
          />
        </Form.Group>
        <Form.Group widths="equal" style={{ width: "50%" }}>
          <Form.Input
            fluid
            label="Frequency"
            value={medication0.frequency}
            name="frequency"
            onChange={this.onMedication0Change}
            placeholder="Frequency"
          />
          <Form.Select
            fluid
            label="Time Period"
            value={medication1.time_period}
            name="time_period"
            onChange={this.onMedication0Change}
            options={periodUnitOptions}
            placeholder="Time Period"
          />
        </Form.Group>
        <br />
        <Form.Input
          fluid
          label="Medication 2"
          value={medication1.med_name}
          name="med_name"
          onChange={this.onMedication1Change}
          placeholder="Medication Name"
          style={{ width: "65%" }}
        />
        <Form.Group widths="equal" style={{ width: "50%" }}>
          <Form.Input
            fluid
            label="Dosage"
            value={medication1.dosage}
            name="dosage"
            onChange={this.onMedication1Change}
            placeholder="Dosage"
          />
          <Form.Select
            fluid
            label="Unit"
            value={medication1.dosageUnit}
            name="dosage_unit"
            onChange={this.onMedication1Change}
            options={dosageUnitOptions}
            placeholder="Unit"
          />
        </Form.Group>
        <Form.Group widths="equal" style={{ width: "50%" }}>
          <Form.Input
            fluid
            label="Frequency"
            value={medication1.frequency}
            name="frequency"
            onChange={this.onMedication1Change}
            placeholder="Frequency"
          />
          <Form.Select
            fluid
            label="Time Period"
            value={medication1.time_period}
            name="time_period"
            onChange={this.onMedication1Change}
            options={periodUnitOptions}
            placeholder="Time Period"
          />
        </Form.Group>
        <Form.Input
          fluid
          label="Medication 3"
          value={medication2.med_name}
          name="med_name"
          onChange={this.onMedication2Change}
          placeholder="Medication Name"
          style={{ width: "65%" }}
        />
        <Form.Group widths="equal" style={{ width: "50%" }}>
          <Form.Input
            fluid
            label="Dosage"
            value={medication2.dosage}
            name="dosage"
            onChange={this.onMedication2Change}
            placeholder="Dosage"
          />
          <Form.Select
            fluid
            label="Unit"
            value={medication2.dosageUnit}
            name="dosage_unit"
            onChange={this.onMedication2Change}
            options={dosageUnitOptions}
            placeholder="Unit"
          />
        </Form.Group>
        <Form.Group widths="equal" style={{ width: "50%" }}>
          <Form.Input
            fluid
            label="Frequency"
            value={medication2.frequency}
            name="frequency"
            onChange={this.onMedication2Change}
            placeholder="Frequency"
          />
          <Form.Select
            fluid
            label="Time Period"
            value={medication2.time_period}
            name="time_period"
            onChange={this.onMedication1Change}
            options={periodUnitOptions}
            placeholder="Time Period"
          />
        </Form.Group>
        <Form.Button onClick={this.handleSubmit}>Submit</Form.Button>
      </Form>
    );
  }
}

export default RegistrationForm;
