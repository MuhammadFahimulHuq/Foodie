import React from 'react'
import MainDisplay from '../Components/MainDisplay'
import MainNavbar from '../Components/MainNavbar'
import RestaurantSection from '../Components/RestaurantSection' 

function Home() {
    return(<div>
        <MainNavbar />
        <MainDisplay />
        <RestaurantSection />
    </div>)
}
export default Home