import { render, screen } from '@testing-library/react';
import OperationalAnalytics from '../../../frontend/src/components/OperationalAnalytics';
import { expect, test } from 'vitest';

test('OperationalAnalytics renders correctly', () => {
  render(<OperationalAnalytics />);
  expect(screen.getByText(/Operational Analytics/i)).toBeDefined();
  expect(screen.getByText(/Total Rides/i)).toBeDefined();
});
