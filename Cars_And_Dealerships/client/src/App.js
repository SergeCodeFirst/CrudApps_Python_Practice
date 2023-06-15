import './App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom'


import Home from './View/Home';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
      </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
