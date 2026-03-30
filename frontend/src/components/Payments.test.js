import React from 'react';
import { render, screen } from '@testing-library/react';
import Payments from './Payments';

test('renders Payments component', () => {
  render(<Payments />);
  const linkElement = screen.getByText(/Payments/i);
  expect(linkElement).toBeInTheDocument();
});
