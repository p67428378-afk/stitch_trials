import { render, screen } from '@testing-library/react';
import UserRoleManagement from '../../../frontend/src/components/UserRoleManagement';
import { expect, test } from 'vitest';

test('UserRoleManagement renders correctly', () => {
  render(<UserRoleManagement />);
  expect(screen.getByText(/Marcus Holloway/i)).toBeDefined();
  expect(screen.getByText(/Lead Dispatcher/i)).toBeDefined();
});
