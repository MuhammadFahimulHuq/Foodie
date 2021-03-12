import React from 'react'
import { Container,Navbar } from 'react-bootstrap'
import {Link} from 'react-router-dom'



function MainNavbar() {

    return(
        <div>   

    <div>
<Navbar fixed="top" expand="xl" variant="light" bg="light" >
 
  <Container>
         <Navbar.Brand> 
           <Link to="/">FOODIE</Link>
           </Navbar.Brand>
          <Navbar.Text>
          join our foodie rider team <Link to="/deliver/registration">Apply now!</Link>
        </Navbar.Text>
       <Link to="/customer/registration">LOGIN</Link>
       
       </Container>
 
      </Navbar>
      
</div>




      
               
      </div>
    )
}
export default MainNavbar

