import React from 'react'
import {useState} from 'react'
import MainNavbar from '../../Components/MainNavbar'
import { Jumbotron,Button, Container,Modal, Form } from 'react-bootstrap';




function RestaurantDashboard(){
    const [showModal, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
  
      

return(
    <div>
        <MainNavbar />
        <Container>
        <Jumbotron>
        <h3>Restaurant Dashboard</h3>

        <p>
            <Button variant="primary" onClick={handleShow}> Add Category</Button>
        </p>
        </Jumbotron>
</Container>

      <Modal show={showModal} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Create a category</Modal.Title>
        </Modal.Header>
        <Form>
        <Modal.Body>Example : Main Platter, Beveage, Sides
        <Form.Group controlId="Category" className='pt-3'>
    <Form.Control type="text" placeholder="Enter category" />
    </Form.Group>
       </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Add
          </Button>
        </Modal.Footer>
        </Form>
      </Modal>

 </div> 
)

}


export default RestaurantDashboard;