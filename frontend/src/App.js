import React, { Component } from 'react';
import {Route, Switch, BrowserRouter} from 'react-router-dom';
import thunk from "redux-thunk";

import PonyNote from "./components/PonyNote";
import NotFound from "./components/NotFound";

import { Provider } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import ponyApp from "./reducers";

let store = createStore(ponyApp, applyMiddleware(thunk));


class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <BrowserRouter>
          <Switch>
            <Route exact path="/" component={PonyNote} />
            <Route component={NotFound} />
          </Switch>
        </BrowserRouter>
      </Provider>
    );
  }
}

export default App;