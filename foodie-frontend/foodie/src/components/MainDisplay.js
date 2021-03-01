import React from 'react'
import {Jumbotron, Container,Form,FormControl,Button,Figure,Image} from 'react-bootstrap'

import RestaurantSection from './RestaurantSection'


function MainDisplay() {
return(
    <div >
      <Container>
      <Jumbotron fluid  >
  <Container >
    <h1 className="pt-5">It's the food you love, delivered</h1>
    </Container>
    <Container>
    <Form inline>
    <FormControl  size="lg" type="text" placeholder="Enter your full address" className=" mr-sm-2" />
    <Button type="submit" className=" mr-sm-2">DELIVERY</Button>
    <h3 className=" mr-sm-2">or</h3>
    <Button type="submit" >PICK UP</Button>
  </Form>
    </Container>
    
  
  </Jumbotron>

 <RestaurantSection />
 
      </Container>
  
    </div>
)

}
export default MainDisplay;