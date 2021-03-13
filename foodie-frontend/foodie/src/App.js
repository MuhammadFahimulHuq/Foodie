
import './App.css'
import Home from './Pages/Home'
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom'
import CustomerRegistration from './Pages/CustomerPage/Registration'
import Profile from './Pages/CustomerPage/Profile';
import DeliverRegistration from './Pages/DeliverPage/Registration'
import RestaurantRegistration from './Pages/RestaurantPage/Registration'
import RestaurantDashboard from './Pages/RestaurantPage/RestaurantDashboard'


function App() {
  return (
  <Router>

<Switch>
<Route path='/restaurant/dashboard' component={RestaurantDashboard} />
<Route path='/restaurant/registration' component={RestaurantRegistration} />
<Route path='/deliver/registration' component={DeliverRegistration} />
<Route path ='/customer/profile' component = {Profile} />
<Route path='/customer/registration' component={CustomerRegistration}/>
<Route path='/' exact component={Home} />

</Switch>

  
  </Router>

  );
}

export default App;
