import React from 'react'
import {useState} from 'react'
import { Container,Card } from 'react-bootstrap';
import Slider from "react-slick";


function Category() {
    function SamplePrevArrow(props) {
        const { className, style, onClick } = props;
        return (
          <div
            className={className}
            style={{ ...style, display: "block", background: "blue" }}
            onClick={onClick}
          />
        );
      }
      function SampleNextArrow(props) {
        const { className, style, onClick } = props;
        return (
          <div
            className={className}
            style={{ ...style, display: "block", background: "blue" }}
            onClick={onClick}
          />
        );
      }



    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1,
        nextArrow: <SampleNextArrow />,
        prevArrow: <SamplePrevArrow />
      }
    return(
        <div>
            <Container>
            <h4> Category</h4>
        <Slider {...settings}>
          <div>
          <Card style={{ width: '18rem' }}>
     <Card.Body>
    <Card.Title>Card Title</Card.Title>
    <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
    <Card.Text>
      Some quick example text to build on the card title and make up the bulk of
      the card's content.
    </Card.Text>
    </Card.Body>
        </Card>
          </div>
          <div>
          <Card style={{ width: '18rem' }}>
    <Card.Body>
    <Card.Title>Card Title</Card.Title>
    <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
    <Card.Text>
      Some quick example text to build on the card title and make up the bulk of
      the card's content.
    </Card.Text>
    </Card.Body>
        </Card>
          </div>
          <div>
          <Card style={{ width: '18rem' }}>
    <Card.Body>
    <Card.Title>Card Title</Card.Title>
    <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
    <Card.Text>
      Some quick example text to build on the card title and make up the bulk of
      the card's content.
    </Card.Text>
     </Card.Body>
        </Card>
          </div>
          <div>
          <Card style={{ width: '18rem' }}>
     <Card.Body>
    <Card.Title>Card Title</Card.Title>
     <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
        <Card.Text>
      Some quick example text to build on the card title and make up the bulk of
      the card's content.
      </Card.Text>
      </Card.Body>
        </Card>
          </div>
        </Slider>
            </Container>
     
        </div>
    )
}
export default Category;