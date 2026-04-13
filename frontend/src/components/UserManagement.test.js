import React from 'react';
import { render, screen } from '@testing-library/react';
import UserManagement from './UserManagement';

test('renders UserManagement component', () => {
  render(<UserManagement />);
  const linkElement = screen.getByText(/User Management/i);
  expect(linkElement).toBeInTheDocument();
});
