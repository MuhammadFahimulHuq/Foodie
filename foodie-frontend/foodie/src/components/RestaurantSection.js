import React from 'react'
import {Jumbotron,Button, Container} from 'react-bootstrap'
import {Link} from 'react-router-dom'


function RestaurantSection(){
return(
<div>
  <Container>
  <Jumbotron>
  <h1>List your restaurant on FOODIE</h1>
  <p>
  Would you like thousands of new customers to taste your amazing food? So would we!
It's simple: we list your menu online, help you process orders, pick them up, and deliver them to hungry pandas - in a heartbeat!
Interested? Let's start our partnership today!
  </p>
  <p>
  <Link to='/restaurant/registration'> <Button variant="primary">Get Started</Button></Link>
  </p>
</Jumbotron>
  </Container>

</div>

)
}
export default RestaurantSection