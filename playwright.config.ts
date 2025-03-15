//npm install @playwright/test
import { PlaywrightTestConfig } from '@playwright/test';

const config: PlaywrightTestConfig = {
  testDir: './tests',
  timeout: 30000,
  retries: 2,
  use: {
    baseURL: 'http://localhost:3000',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  reporter: [
    ['html'],
    ['junit', { outputFile: 'test-results/junit.xml' }]
  ]
};

export default config;

//npx playwright test loan-application.spec.ts