import { render, screen } from '@testing-library/react';
import Navbar from '../../../frontend/src/components/Navbar';
import { expect, test } from 'vitest';

test('Navbar renders correctly', () => {
  render(<Navbar />);
  expect(screen.getByText(/Fleet Control Center/i)).toBeDefined();
  expect(screen.getByText(/Dispatch Hub/i)).toBeDefined();
});
