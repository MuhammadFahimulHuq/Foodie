import React from 'react'
import {useState} from 'react'
import { Container,Form,Button, Col,Row } from 'react-bootstrap'
import MainNavbar from '../../Components/MainNavbar'
import axios from 'axios'



function Registration() {
    const[restaurantRegistration, setRestaurantRegistration] = useState({
        user:{
            first_name:'',
            last_name:'Owner Last Name',
            username:'Restaurant Name',
            email:'Email',
            password:'Password',
            address:'',
            dateOfBirth:'',
            phoneNo:'Contact Number',
        },
        description:'Write About Your Restaurant'
    })
    const userHandleChange =(event)=>{
        setRestaurantRegistration({
            ...restaurantRegistration,user:{
                ...restaurantRegistration.user,
                [event.target.name]:event.target.value
            }
        })
    }
    const descriptionHandleChange=(event)=>{
        setRestaurantRegistration({
            ...restaurantRegistration,
            [event.target.name]:event.target.value
        })
    }
    const handleSubmit =(e) =>{
        e.preventDefault()
        axios.post('http://127.0.0.1:8000/restaurant/registration/',restaurantRegistration)
          .then((response) => {
            console.log(response)
          })
          .catch((error)=>{
            console.log(error)
          })
      }
    
    return(<div>
  <MainNavbar />
           
           <Container className="pt-5">
             <Row>
             <Col  xs="6" sm="4">

             <h4>Restaurant Registation Form</h4>
           <Form onSubmit={handleSubmit} >
 <Form.Group controlId="user.first_name">
   <Form.Control type="Text" placeholder="Owner First Name" name="first_name" value={restaurantRegistration.first_name} onChange={userHandleChange}  />
 </Form.Group>
 <Form.Group controlId="user.last_name">
   <Form.Control type="Text"  placeholder="Owner Last Name" name="last_name" value={restaurantRegistration.last_name} onChange={userHandleChange}  />
 </Form.Group>
 <Form.Group controlId="user.username">
   <Form.Control type="Text"   placeholder="Restaurant Name" name="username" value={restaurantRegistration.username} onChange={userHandleChange}  />
 </Form.Group>
 <Form.Group controlId="user.email">
   <Form.Control type="Text"  placeholder="Restaurant Email" name="email" value={restaurantRegistration.email} onChange={userHandleChange}  />
 </Form.Group>
 <Form.Group controlId="user.password">
   <Form.Control type="password" placeholder="Password" name="password"  value={restaurantRegistration.password} onChange={userHandleChange} />
 </Form.Group>
 <Form.Group controlId="user.address">
   <Form.Label>Restaurant Address</Form.Label>
   <Form.Control as="textarea" rows={3} name="address" value={restaurantRegistration.address} onChange={userHandleChange} />
 </Form.Group>

 <Form.Group controlId="user.phoneNo">
   <Form.Control type="number"  placeholder="Resturant Contact No"  name="phoneNo" value={restaurantRegistration.phoneNo} onChange={userHandleChange}  />
 </Form.Group>
 <Form.Group controlId="user.dateOfBirth">
     <Form.Label>Restaurant Founded In</Form.Label>
   <Form.Control type="date" name="dateOfBirth" value={restaurantRegistration.dateOfBirth} onChange={userHandleChange}  />
 </Form.Group>
 <Form.Group controlId="description">
   <Form.Label>Description</Form.Label>
   <Form.Control as="textarea" rows={3} name="description" value={restaurantRegistration.description} onChange={descriptionHandleChange} />
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
    </div>)
}
export default Registration;