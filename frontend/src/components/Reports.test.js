import React from 'react';
import { render, screen } from '@testing-library/react';
import Reports from './Reports';

test('renders Reports component', () => {
  render(<Reports />);
  const linkElement = screen.getByText(/Reports/i);
  expect(linkElement).toBeInTheDocument();
});
