import { render, screen } from '@testing-library/react';
import App from './App';

test('renders the landing page on initial load', () => {
  render(<App />);
  // Step 0 renders <Landing />; adjust this text to match your actual
  // Landing.js heading/CTA copy if it differs.
  const heading = screen.getByRole('heading', { level: 1 });
  expect(heading).toBeInTheDocument();
});