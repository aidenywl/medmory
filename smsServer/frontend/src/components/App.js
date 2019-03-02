import React from "react";

class App extends React.Component {
  render() {
    return (<div> 


 <form>
  First name:
  <input type="text" name="firstname"/>< br />
  Last name:
  <input type="text" name="lastname"/>< br />
  Phone number:
  <input type="text" name="lastname"/>< br />
  <input type="radio" name="gender" value="male" checked/> Male
  <input type="radio" name="gender" value="female"/> Female
  <input type="radio" name="gender" value="other"/> Other< br />
  Medication Name:
  <input type="text" name="medication"/>< br />
  Dosage:
  <input type="text" name="dosage"/>< br />
  Frequency:
  <input type="text" name="dosage"/>< br />
  Time Period:
  <input type="text" name="dosage"/>< br />  
    
</form>  

  </div>);
  }
}

export default App;
