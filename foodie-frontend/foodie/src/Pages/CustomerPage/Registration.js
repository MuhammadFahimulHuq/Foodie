import React from 'react'
import { Container,Form,Button } from 'react-bootstrap'
import MainNavbar from '../../Components/MainNavbar'


function Registration() {
    return(
        <div>
        <div>
        <MainNavbar /></div>
            <div>
           
            <Container className="pt-5">
            <h1> Registation Form</h1>
            <Form>
  <Form.Group controlId="Customer_Email">
    <Form.Control type="Text" placeholder="Full Name" />
  </Form.Group>
  <Form.Group controlId="Customer_Password">
    <Form.Control type="password" placeholder="Password" />
  </Form.Group>
  <Form.Group controlId="Customer_Address">
    <Form.Control type="Text" placeholder="Address" />
  </Form.Group>
  <Form.Group controlId="Customer_PhoneNo">
    <Form.Control type="number" placeholder="Phone Number" />
  </Form.Group>
  <Form.Group controlId="Customer_PhoneNo">
      <Form.Label>Date Of Birth</Form.Label>
    <Form.Control type="datetime-local" />
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