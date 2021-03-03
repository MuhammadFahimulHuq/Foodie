
import './App.css'
import Home from './Pages/Home'
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom'
import Registration from './Pages/CustomerPage/Registration'
import Profile from './Pages/CustomerPage/Profile';


function App() {
  return (
  <Router>

<Switch>
<Route path ='/customer/profile' component = {Profile} />
<Route path='/customer/registration' component={Registration}/>
<Route path='/' exact component={Home} />

</Switch>

  
  </Router>

  );
}

export default App;
