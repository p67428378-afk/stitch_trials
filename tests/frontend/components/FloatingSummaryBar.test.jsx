import { render, screen } from '@testing-library/react';
import FloatingSummaryBar from '../../../frontend/src/components/FloatingSummaryBar';
import { expect, test } from 'vitest';

test('FloatingSummaryBar renders correctly', () => {
  render(<FloatingSummaryBar />);
  expect(screen.getByText(/SYSTEM STATUS:/i)).toBeDefined();
  expect(screen.getByText(/Quick Dispatch/i)).toBeDefined();
});
