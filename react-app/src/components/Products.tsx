import axios from 'axios';
import React from 'react';
import { Component } from 'react';

export default class Products extends Component {
  state = {
    products: [],
  };

  public componentDidMount() {
    axios.get(`http://www.mocky.io/v2/5c811f3b310000c016771d9b`).then(response => {
      const products = response.data;
      console.log(products);
      this.setState({ products });
    });
  }

  public render() {
    return (
      <ul>
        { this.state.products.map(product => <li>{product.name}</li>)}
      </ul>
    );
  }
}
