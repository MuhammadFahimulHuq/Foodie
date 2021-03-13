import React from 'react'
import {useState} from 'react'
import MainNavbar from '../../Components/MainNavbar'
import { Jumbotron,Button, Container,Modal, Form } from 'react-bootstrap';
import axios from 'axios';
import Category from '../../Components/CategorySection';



function RestaurantDashboard(){
    const [showModal, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const[categoryInput,setCategoryInput] = useState({
      name:'',
    })
    const handleChange=(event)=>{
      setCategoryInput({
        ...categoryInput,
        [event.target.name]:event.target.value
    })
    }
    const handleSubmit=(e)=>{
      e.preventDefault()
      axios.post('http://127.0.0.1:8000/restaurant/category/create/',categoryInput)
        .then((response)=>{
          console.log(response)
        })
        .catch((error)=>{
          console.log(error)
        })
    }
      

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
        <Form onSubmit={handleSubmit}> 
        <Modal.Body>Example : Main Platter, Bevarage, Sides
        <Form.Group controlId="Category" className='pt-3'>
    <Form.Control type="text" placeholder="Enter category" name="name" value={categoryInput.name} onChange={handleChange}/>
    </Form.Group>
       </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" type="submit">
            Add
          </Button>
        </Modal.Footer>
        </Form>
      </Modal>
<Category />
 </div> 
)

}


export default RestaurantDashboard;