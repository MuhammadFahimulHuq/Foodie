import React from 'react'
import { Container,Form,Button } from 'react-bootstrap'
import MainNavbar from '../../Components/MainNavbar'
import axios from 'axios'
import { useState } from 'react'



function Registration()  {
  const[ customerRegistration,setCustomerRegistration] =useState({
    customer_name: '',
    customer_email:'',
    customer_password:'',
    customer_address:'',
    customer_phoneNo:'',
    customer_dateOfBirth:'',
  })
 
const handleChange = (event) =>{
  setCustomerRegistration({
    ...customerRegistration,
[event.target.name] :event.target.value
  })
}
const handleSubmit =(e) =>{
  e.preventDefault()
  axios.post('http://127.0.0.1:8000/customer/registration/',customerRegistration)
    .then((response) => {
      console.log(response)
    })
    .catch((error)=>{
      console.log(error)
    })
}


 


    return(
        <div>
        <div>
        <MainNavbar /></div>
            <div>
           
            <Container className="pt-5">
            <h1> Registation Form</h1>
            <Form onSubmit={handleSubmit}>
  <Form.Group controlId="Customer_fullName">
    <Form.Control type="Text" placeholder="Full Name" name="customer_name" value={customerRegistration.customer_name} onChange={handleChange}  />
  </Form.Group>
  <Form.Group controlId="Customer_Email">
    <Form.Control type="Text" placeholder="Email" name="customer_email" value={customerRegistration.customer_email} onChange={handleChange}  />
  </Form.Group>
  <Form.Group controlId="Customer_Password">
    <Form.Control type="password" placeholder="Password" name="customer_password"  value={customerRegistration.customer_password} onChange={handleChange} />
  </Form.Group>
  <Form.Group controlId="Customer_Address">
    <Form.Control type="Text" placeholder="Address" name="customer_address" value={customerRegistration.customer_address} onChange={handleChange} />
  </Form.Group>
  <Form.Group controlId="Customer_PhoneNo">
    <Form.Control type="number" placeholder="Phone Number" name="customer_phoneNo" value={customerRegistration.customer_phoneNo} onChange={handleChange}  />
  </Form.Group>
  <Form.Group controlId="Customer_Date">
      <Form.Label>Date Of Birth</Form.Label>
    <Form.Control type="datetime-local" name="customer_dateOfBirth" value={customerRegistration.customer_dateOfBirth} onChange={handleChange}  />
  </Form.Group>
  <Form.Group>
    <Form.File id="Customer_profilePicture" label="Upload Profile Picture" />
  </Form.Group>

  <Button variant="primary" type="submit">
    Submit
  </Button>
</Form>
            </Container>

            </div>
          
          
           
        </div>
    )
}
export default Registration;