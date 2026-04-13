import React from 'react';
import { render, screen } from '@testing-library/react';
import LiveMap from './LiveMap';

test('renders LiveMap component', () => {
  render(<LiveMap />);
  const linkElement = screen.getByText(/Live Map/i);
  expect(linkElement).toBeInTheDocument();
});
