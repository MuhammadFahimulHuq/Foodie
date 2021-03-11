import React from 'react'
import { Container,Form,Button, Col,Row } from 'react-bootstrap'
import MainNavbar from '../../Components/MainNavbar'
import axios from 'axios'
import { useState } from 'react'



function Registration()  {
  const[ customerRegistration,setCustomerRegistration] =useState({
    user:{
      first_name:'',
      last_name:'',
      username:'',
      email:'',
      password:'',
      address:'',
      dateOfBirth:'',
      phoneNo:'',
    
    }
   


  })
 
const handleChange = (event) =>{
  setCustomerRegistration({
    ...customerRegistration,user:{
      ...customerRegistration.user,
      [event.target.name] :event.target.value
    } 

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
        <MainNavbar />
           
            <Container className="pt-5">
              <Row>
              <Col  xs="6" sm="4">

              <h1> Registation Form</h1>
            <Form onSubmit={handleSubmit} >
  <Form.Group controlId="user.first_name">
    <Form.Control type="Text" placeholder="First Name" name="first_name" value={customerRegistration.first_name} onChange={handleChange}  />
  </Form.Group>
  <Form.Group controlId="user.last_name">
    <Form.Control type="Text" placeholder="Last Name" name="last_name" value={customerRegistration.last_name} onChange={handleChange}  />
  </Form.Group>
  <Form.Group controlId="user.username">
    <Form.Control type="Text" placeholder="Username" name="username" value={customerRegistration.username} onChange={handleChange}  />
  </Form.Group>
  <Form.Group controlId="user.email">
    <Form.Control type="Text" placeholder="Email" name="email" value={customerRegistration.email} onChange={handleChange}  />
  </Form.Group>
  <Form.Group controlId="user.password">
    <Form.Control type="password" placeholder="Password" name="password"  value={customerRegistration.password} onChange={handleChange} />
  </Form.Group>
  <Form.Group controlId="user.address">
    <Form.Label>Address</Form.Label>
    <Form.Control as="textarea" rows={3} name="address" value={customerRegistration.address} onChange={handleChange} />
  </Form.Group>

  <Form.Group controlId="user.phoneNo">
    <Form.Control type="number" placeholder="Phone Number" name="phoneNo" value={customerRegistration.phoneNo} onChange={handleChange}  />
  </Form.Group>
  <Form.Group controlId="user.dateOfBirth">
      <Form.Label>Date Of Birth</Form.Label>
    <Form.Control type="date" name="dateOfBirth" value={customerRegistration.dateOfBirth} onChange={handleChange}  />
  </Form.Group>
  <Form.Group>
    <Form.File id="Customer_profilePicture" label="Upload Profile Picture" name="customer_profilePicture"  />
  </Form.Group>

  <Button variant="primary" type="submit">
    Submit
  </Button>
</Form>
            

                  </Col>
              </Row>
         
              </Container>

          
           
        </div>
    )
}
export default Registration;