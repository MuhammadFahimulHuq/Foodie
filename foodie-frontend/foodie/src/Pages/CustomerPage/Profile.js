import React from 'react'
import { Col, Container, Row,Form,Button } from 'react-bootstrap'
import MainNavbar from '../../Components/MainNavbar'

function Profile() {
    return(
<div>
    <MainNavbar />
        <Container>
            <Row>
                <Col>
                </Col>
                <Col>
                <h4>
                    MY PROFILE
                </h4>
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
    SAVE
  </Button>
  </Form> 
                </Col>
                <Col>
                </Col>
            </Row>
        </Container>
  
</div>

    )

}
export default Profile;