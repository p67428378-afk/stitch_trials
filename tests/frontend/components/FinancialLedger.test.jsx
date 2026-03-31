import { render, screen } from '@testing-library/react';
import FinancialLedger from '../../../frontend/src/components/FinancialLedger';
import { expect, test } from 'vitest';

test('FinancialLedger renders correctly', () => {
  render(<FinancialLedger />);
  expect(screen.getByText(/Financial Ledger/i)).toBeDefined();
  expect(screen.getByText(/Recent Transactions/i)).toBeDefined();
});
