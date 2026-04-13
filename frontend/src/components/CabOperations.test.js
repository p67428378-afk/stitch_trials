import React from 'react';
import { render, screen } from '@testing-library/react';
import CabOperations from './CabOperations';

test('renders CabOperations component', () => {
  render(<CabOperations />);
  const linkElement = screen.getByText(/Cab Operations/i);
  expect(linkElement).toBeInTheDocument();
});
