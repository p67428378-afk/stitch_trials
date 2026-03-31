import { render, screen } from '@testing-library/react';
import DispatchControl from '../../../frontend/src/components/DispatchControl';
import { expect, test } from 'vitest';

test('DispatchControl renders correctly', () => {
  render(<DispatchControl />);
  expect(screen.getByText(/New Booking/i)).toBeDefined();
  expect(screen.getByText(/Pending Dispatches/i)).toBeDefined();
});
