import { render, screen } from '@testing-library/react';
import RealtimeTracking from '../../../frontend/src/components/RealtimeTracking';
import { expect, test } from 'vitest';

test('RealtimeTracking renders correctly', () => {
  render(<RealtimeTracking />);
  expect(screen.getByText(/Global Live Operations/i)).toBeDefined();
  expect(screen.getByText(/Ride Progress/i)).toBeDefined();
});
