import { render, screen } from '@testing-library/react';
import Sidebar from '../../../frontend/src/components/Sidebar';
import { expect, test } from 'vitest';

test('Sidebar renders correctly', () => {
  render(<Sidebar />);
  expect(screen.getByText(/Lead Dispatcher/i)).toBeDefined();
  expect(screen.getByText(/Dispatch Hub/i)).toBeDefined();
});
