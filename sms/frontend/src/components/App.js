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
  <input type="text" name="phonenumber"/>< br />
  
  Gender:
  <input type="radio" name="gender" value="male" checked/> Male
  <input type="radio" name="gender" value="female"/> Female
  <input type="radio" name="gender" value="other"/> Other< br />
  
  Medication Name:
  <input type="text" name="medication"/>< br />
  
  Dosage:
  <input type="text" name="dosage"/>
  
  Unit:
  <select>
  <option value="mg">mg</option>
  <option value="mL">mL</option>
  </select>
  < br />
  
  Frequency:
  <select>
  <option value="1">1x</option>
  <option value="2">2x</option>
  <option value="3">3x</option>
  <option value="4">4x</option>
  <option value="5">5x</option>
  <option value="6">6x</option>
  <option value="7">7x</option>
  <option value="8">8x</option>
  <option value="9">9x</option>
  <option value="10">10x</option>
  <option value="11">11x</option>
  <option value="12">12x</option>
  <option value="10">13x</option>
  <option value="11">14x</option>
  <option value="12">15x</option>
  </select> 
  
  Time Period:
  <select>
  <option value="daily">Daily</option>
  <option value="weekly">Weekly</option>
  <option value="bi-weekly">Bi-Weekly</option>
  <option value="monthly">Monthly</option>
  </select> 
   
</form>  

  </div>);
  }
}

export default App;
